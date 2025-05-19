from flask import Flask, jsonify, redirect, request, url_for, session
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

CORS(app)

oauth = OAuth(app)

nonce = generate_token()

client = MongoClient('mongodb://root:rootpassword@mongo:27017/mydatabase?authSource=admin')
db = client["mydatabase"]
comments = db["comments"]

oauth.register(
    name=os.getenv('OIDC_CLIENT_NAME'),
    client_id=os.getenv('OIDC_CLIENT_ID'),
    client_secret=os.getenv('OIDC_CLIENT_SECRET'),
    #server_metadata_url='http://dex:5556/.well-known/openid-configuration',
    authorization_endpoint="http://localhost:5556/auth",
    token_endpoint="http://dex:5556/token",
    jwks_uri="http://dex:5556/keys",
    userinfo_endpoint="http://dex:5556/userinfo",
    device_authorization_endpoint="http://dex:5556/device/code",
    client_kwargs={'scope': 'openid email profile'}
)

# code from lecture Notes -> updated it so it works for comments section in mongo comprass 
@app.route('/api/comments/<string:commentID>', methods=['GET'])
def getComments(commentID):
    #differentComment = list(comments.find())
    differentComment = list(comments.find({"commentID": commentID})) # need to check which id it's 
    for comment in differentComment:
        comment['_id'] = str(comment['_id'])
    return jsonify(differentComment)


# needed to add commentID so that it would send the right comments to right sidebar
@app.route('/api/inputData/<string:commentID>', methods=['POST'])
def addData(commentID):
    data = request.json or {}
    comment_text = data.get('comment', "This is a test comment")
    comments.insert_one({
        'comment': comment_text,
        'commentID': commentID # added this section to mongo
    })
    return '', 201

@app.route('/api/key')
def get_key():
    return jsonify({'apiKey': os.getenv('NYT_API_KEY')})

@app.route('/')
def home():
    user = session.get('user')
    if user:
        return f"<h2>Logged in as {user['email']}</h2><a href='/logout'>Logout</a>"
    return '<a href="/login">Login with Dex</a>'

@app.route('/login')
def login():
    session['nonce'] = nonce
    redirect_uri = 'http://localhost:8000/authorize' # will redirect to authorize 
    return oauth.flask_app.authorize_redirect(redirect_uri, nonce=nonce)

@app.route('/authorize')
def authorize():
    token = oauth.flask_app.authorize_access_token()
    nonce = session.get('nonce')

    user_info = oauth.flask_app.parse_id_token(token, nonce=nonce)  # or use .get('userinfo').json()
    session['user'] = user_info
    return redirect(f"http://localhost:5173/loggedIn")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('http://localhost:5173')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

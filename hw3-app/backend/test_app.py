import pytest
from app import app as mainApp
import os
from unittest.mock import patch

# source used https://flask.palletsprojects.com/en/stable/testing/
# https://docs.pytest.org/en/stable/how-to/index.html

# getting the testing evn started with client 
@pytest.fixture()
def client():
    mainApp.config.update({
        "TESTING": True,
    })
    return mainApp.test_client()

@pytest.fixture()
def runner():
    return mainApp.test_cli_runner()

#making sure the log in worked + same as the app.py 
def test_loginWorks(client):
    res = client.get("/")
    assert b"Login with Dex" in res.data

# checking if the main page worked 
def test_MainPageStatus(client):
    res = client.get("/")
    assert res.status_code == 200

# making sure the status is the redirection 
def test_logoutWorked(client):
    res = client.get("/logout")
    assert res.status_code == 302 

# funny tests to make sure it no work cause no bananan
def test_NotWorkServer(client):
    res = client.get('/banana')
    assert res.status_code == 404

# again checking it no work 
def test_randomFile(client):
    res = client.get('/random/file')
    assert res.status_code == 404

# if the api key is being given from env right
def test_apiKeyWorks(client):
    os.environ["NYT_API_KEY"] = "newkey"
    res = client.get("/api/key")
    assert res.get_json() == {"apiKey": "newkey"}

# checking if the api status worked or nah 
def test_apiStatus(client):
    os.environ["NYT_API_KEY"] = "newkey"
    res = client.get("/api/key")
    assert res.status_code == 200

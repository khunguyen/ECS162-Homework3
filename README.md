Homework 3: Ananya Ratakonda and Khanh Nguyen

Please note that there is no .env file attached and you must provide you own which should include a NYT_API_KEY and PORT number.

Frontend Dependencies: 
```
cd frontend
-npm install 
-npm -D vitest 
-npm -D jsdom 
-npm install -D vitest @testing-library/jest-dom
```

Backend Dependencies: 
```
python3 -m pip install pytest
```
The docker-compose build we used was the development version and was built using the following command: 
```
docker compose -f 'docker-compose.dev.yml' up -d --build
```

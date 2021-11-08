# Hands on [flask-sock](https://github.com/miguelgrinberg/flask-sock) package by [Miguel Grinberg](https://github.com/miguelgrinberg)

## Run server
- `gunicorn -b localhost:5000 --workers 2 --threads 8 "main:create_app()"`
- Connect to ws://localhost:5000/caesor-cipher

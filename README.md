[![Maintainability](https://api.codeclimate.com/v1/badges/f1a635f6ddbfbf7ea19b/maintainability)](https://codeclimate.com/github/FarDust/we-may-chat/maintainability) <a href="https://gitmoji.carloscuesta.me">
  <img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square" alt="Gitmoji">
</a>

# We May Chat

A simple anonymous chat

## App Summary

This is a small app that simply works using Django as API, [socket.io](https://socket.io) as comunication protocol and Angular as frontend single page web app.
I'm using sqlite as database for the app but any SQL database may work as well.

Most of the comunication is over /socket.io/ endpoint.

## Development instructions

- (Optional) prepare virtualenv with [pipenv](https://pipenv-es.readthedocs.io/es/latest/)
- Install dependencies: `pip install -r requirements.txt`
- Run app: `python manage.py runserver`
- Open `localhost:8000` in web browser

## Disclaimer

this app is not meant to be production ready

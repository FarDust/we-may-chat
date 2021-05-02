[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

[![Maintainability](https://api.codeclimate.com/v1/badges/f1a635f6ddbfbf7ea19b/maintainability)](https://codeclimate.com/github/FarDust/we-may-chat/maintainability)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/FarDust/we-may-chat.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/FarDust/we-may-chat/alerts/)
[![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/FarDust/we-may-chat.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/FarDust/we-may-chat/context:javascript)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/FarDust/we-may-chat.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/FarDust/we-may-chat/context:python)

# We May Chat

A simple anonymous chat

## App Summary

This is a small app that simply works using Django as API, [socket.io](https://socket.io) as comunication protocol and Angular as frontend single page web app.
I'm using sqlite as database for the app but any SQL database may work as well.

Most of the comunication is over /socket.io/ endpoint.

## Development instructions

- Prepare virtualenv with [pipenv](https://pipenv-es.readthedocs.io/es/latest/)
- Install dependencies: `pipenv install`
- Install [angular cli](https://angular.io/cli): `npm install -g @angular/cli`
- Change directory `frontend/chat-room`
- Run `npm install`
- Change directory to project root
- Run app: `python manage.py runserver`
- Open `localhost:8000` in web browser

## Disclaimer

this app is not meant to be production ready

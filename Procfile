python manage.py migrate
web: gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 chat.wsgi
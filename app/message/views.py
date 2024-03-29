import json
import os

import socketio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv

from app.message.serializers import MessageSerializer

from .models import Message

load_dotenv()

async_mode = os.getenv('ASYNC_MODE')
sio = socketio.Server(logger=True, async_mode=async_mode)


@csrf_exempt
def get_data(request):
    data = Message.objects.all().order_by('-timestamp')[:100]
    if request.method == 'GET':
        serializer = MessageSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.on('chat-message')
def my_message(sid, data):
    data = json.loads(data)
    if data['content'] != '':
        context = {
            'status': 200,
        }
        context.update(data)
        new_message = Message(**data)
        new_message.save()
        context['timestamp'] = str(new_message.timestamp.timestamp())
        sio.emit('chat-message', json.dumps(context))


@sio.event
def disconnect(sid):
    print('disconnect', sid)

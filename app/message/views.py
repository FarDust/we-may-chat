from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app.message.serializers import MessageSerializer

import socketio
import json
import os


from .models import Message

sio = socketio.Server(async_mode='threading', cors_allowed_origins='*')

# Create your views here.

@csrf_exempt
def new_message(request):
    post_data = request.POST.copy()
    content = post_data['content']
    context = {
        'status': 200,
    }
    data = {
        'content': content,
    }
    context.update(data)
    if request.session.get('nickname', False):
        data['session'] = request.session
    new_message = Message(**data)
    new_message.save()
    context['timestamp'] = str(new_message.timestamp.timestamp())
    return HttpResponse(json.dumps(context), content_type="text/json")

@csrf_exempt
def get_data(request):
    data = Message.objects.all()
    if request.method == 'GET':
        serializer = MessageSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.on('chat-message')
def my_message(sid, data):
    sio.emit('chat-message', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

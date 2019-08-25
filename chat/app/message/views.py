from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Message

# Create your views here.

def new_message(request):
    post_data = request.POST.copy()
    content = post_data['content']
    context = dict()
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
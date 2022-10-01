from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .utils import message_creater
from . import Line_message
from .models import Users
# Create your views here.


def index(request):
    context = {}
    return render(request, 'reply/index.html', context)


def login(request):
    name = request.GET('name')
    password = request.GET('pass')
    login = Users.objects.filter(name=name, password=password)
    return render(request, 'reply/', {})


def pre_register(request):
    context = {}
    return render(request, 'reply/register.html', context)


def register(request):
    name = request.GET['name']
    password = request.GET['password']
    line_id = request.GET['line_id']
    regist = Users(name=name, password=password, line_id=line_id)
    regist.save()
    return render(request, 'reply/index.html', {})


@csrf_exempt
def main(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token = data['replyToken']
        line_message = Line_message(
            message_creater.create_single_text_message(message['text']))
        line_message.reply(reply_token)
        return HttpResponse("ok")

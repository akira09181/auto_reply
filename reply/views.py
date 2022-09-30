from django.shortcuts import render
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

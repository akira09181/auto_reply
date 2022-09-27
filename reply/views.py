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

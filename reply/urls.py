from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pre_register", views.pre_register, name="pre_register"),
    path("register", views.register, name="register"),
    path("main_recieve", views.main_recieve, name="main_recieve"),
]

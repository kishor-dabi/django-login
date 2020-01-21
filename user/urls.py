from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('login', views.login_request, name='login'),
    path('register', views.register),
]

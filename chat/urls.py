# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat_test/', views.chat_test, name='chat_test'),
]

from django.urls import path
from .views import ChatBotView

urlpatterns = [
    path('api/chatbot/', ChatBotView.as_view(), name='chatbot-api-view'),
]
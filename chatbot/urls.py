from django.urls import path, include
from .action.action_views import ChatBotAPIView
from .views import ChatBotView

actions_urlpatterns = [
    path('api/chatbot/', ChatBotAPIView.as_view(), name='chatbot-api-view'),
]

urlpatterns = [
    path('actions/', include(actions_urlpatterns)),
    path('chatbot/', ChatBotView.as_view(), name='chatbot-view'),
]
from django.urls import path, include
from .action.action_chatbot_views import ChatBotAPIView
from .action.action_views import ProductListAPIView, TestAPIView
from .views import ChatBotView

actions_urlpatterns = [
    path('api/chatbot/', ChatBotAPIView.as_view(), name='chatbot-api-view'),
    path('api/products/', ProductListAPIView.as_view(), name='product-list-api-view'),
    path('api/test/', TestAPIView.as_view(), name='test-api=view')
]

urlpatterns = [
    path('actions/', include(actions_urlpatterns)),
    path('chatbot/', ChatBotView.as_view(), name='chatbot-view'),
]
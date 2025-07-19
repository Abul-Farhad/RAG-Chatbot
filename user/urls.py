from django.urls import path

from .views import (
    LoginView,
    LogoutView,
    RegisterView,
)

urlpatterns = [

    path('', LoginView.as_view(), name='user-login'),
    path('register/', RegisterView.as_view(), name='user-register'),
    path('logout/', LogoutView.as_view(), name='user-logout'),

]
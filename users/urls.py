from django.urls import path
from .api.views import UserCreateView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]
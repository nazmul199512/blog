from django.urls import path
from authentication.views import register, user_login, user_logout

app_name = 'authentication'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
     ]

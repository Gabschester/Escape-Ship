from django.urls import path
from appTwo import views

app_name = 'appTwo'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
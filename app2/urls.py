from django.urls import path
from .views import user_login,register

urlpatterns = [
    path('user_login',user_login,name='user_login'),
    path('register', register, name="register"),

]

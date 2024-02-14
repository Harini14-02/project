from django.urls import path
from .views import home, home1

urlpatterns = [
    path('', home, name='home'),
    path('home', home, name='home'),
    path('home1',home1,name='home1'),
]

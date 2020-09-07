from django.urls import path
from .views import register
from . import views


app_name = 'register'

urlpatterns = [
        path('', views.register, name='signup'),
]
from django.urls import path
#from .views import register
from . import views
from .views import SignUpView

app_name = 'register'

urlpatterns = [
        path('', SignUpView.as_view(), name='signup'),
]
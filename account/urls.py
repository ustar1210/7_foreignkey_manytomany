from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("logout/", logout, name="logout"),
]

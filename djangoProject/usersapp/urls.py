from django.urls import path
from usersapp.views import get_username,get_name

urlpatterns = [
    path("users/",get_username),
    path("name/",get_name,name='name'),
]

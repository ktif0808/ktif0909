from django.urls import path
from display import views


urlpatterns = [
    path('', views.index, name="index"),
    path('ip', views.getIP, name="getIP"),
    path('ajax/getUsers', views.getUsers, name = "getUsers"),
]

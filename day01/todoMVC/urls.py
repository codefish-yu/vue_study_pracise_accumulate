from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    #127.0.0.1:8000/todoMVC/vue
    url(r'^vue$',views.todoMVC_vue),
]

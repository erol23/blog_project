from django.urls import path
from .views import post_list, post_create


app_name='blogapp'
urlpatterns = [
    path("", post_list, name='list'),
    path("create", post_create, name='create')
]
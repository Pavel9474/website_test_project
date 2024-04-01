from django.urls import path
from . import views

urlpatterns = [
    path('', views.databones_home, name='databones_home'),
    path('create', views.create, name='create'),
]
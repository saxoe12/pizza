from django.urls import path
from .import views

app_name = 'menu'
urlpatterns = [
    path('', views.index, name='index'),
]
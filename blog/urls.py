from django.urls import path
#importa todas as views do projeto
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
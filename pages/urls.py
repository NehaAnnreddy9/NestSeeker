#Bring path pckg in to use paths
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about')
]
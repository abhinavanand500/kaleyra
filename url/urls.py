from django.urls import include, path
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('get',views.get,name='get'),
    path('showAll',views.showAll,name='all'),
    path('<str:slug>', views.aa, name='slug'),
]

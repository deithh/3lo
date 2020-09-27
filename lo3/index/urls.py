from django.conf.urls import url
from . import views 
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

app_name = 'index'  # przestrzeń nazw aplikacji
urlpatterns = [
    url(r'^$', views.index, name='index'),]
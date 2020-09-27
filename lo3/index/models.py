from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.
"""class spotter(models.Model):
    #Od_Spottera = models.BooleanField()
    #Od_Spoterki = models.BooleanField()
    Od_Spottera = 'Od Spottera'
    Od_Spotterki = 'Od Spotterki'"""
class ContactForm(models.Model):
    wiadomość = models.CharField(max_length=500) ##niepotrzebna klasa meta
    spotter = [
        ('Od_Spottera', 'Od Spottera'),
        ('Od_Spotterki','Od Spotterki'),
    ]
    email = models.EmailField()
    płeć = models.CharField(choices=spotter, max_length=500)
    

class spotted(ModelForm):
    class Meta:
        model= ContactForm
        fields = ['wiadomość', 'email', 'płeć']
    
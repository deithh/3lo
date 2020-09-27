from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.
class ContactForm(models.Model):
    content = models.CharField(max_length=500)
    email = models.EmailField()
    sex = models.BooleanField()
class spotted(ModelForm):
    class Meta:
        model= ContactForm
        fields = ['content', 'email', 'sex']
    
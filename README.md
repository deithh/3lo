
<!--
# 3lo
#026380 niebieski
#ffc011 żółty
#fffdfc jasny

{% load static %}
<html>
  <body>
    <h1>Rejestracja użytkownika</h1>
    {% if user.is_authenticated %}
      <p>Jesteś już zarejestrowany jako {{ user.username }}.
      <br /><a href="/">Strona główna</a></p>
    {% else %}
    <form method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">Zarejestruj</button>
    </form>
    {% endif %}
  </body>
</html>

{% load static %}

//forms.py
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
-->
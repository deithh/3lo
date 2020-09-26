from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


from .forms import RegisterForm
# Create your views here.

def index(request): 
    return render(request, "index/index.html",)
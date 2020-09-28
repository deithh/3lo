from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from .models import ContactForm
from .models import spotted
from django.http import HttpResponse


# Create your views here.
def after(request):
    return render(request, "after.html")
def index(request): 
    
   
    if request.method == 'POST':
        form = spotted(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index:after')

    kontekst = {'form': spotted()}
    
    return render(request, "index.html", kontekst)

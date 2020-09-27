from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from .models import ContactForm
from .models import spotted
from django.http import HttpResponse


# Create your views here.
def wysłano(request):
    return HttpResponse("wysłano")
def index(request): 
    
   
    if request.method == 'POST':
        form = spotted(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect(reverse('index:index'))

    kontekst = {'form': spotted()}
    
    return render(request, "index.html", kontekst)

from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages



# Create your views here.
 
def index(request): 
    
    from .models import spotted
    if request.method == 'POST':
        form = spotted(request, request.POST)
        if form.is_valid():
            
            return redirect(reverse('login:index'))

    kontekst = {'form': spotted()}
    
    return render(request, "index.html", kontekst)
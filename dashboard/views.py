from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here (contact).

def dashboard(request):
    template  = loader.get_template('dashboard.html')
    return HttpResponse(template.render())

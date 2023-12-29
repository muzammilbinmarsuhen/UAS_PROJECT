from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here (dashboard).
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    
    template  = loader.get_template('dashboard.html')
    return HttpResponse(template.render())


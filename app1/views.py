from django.shortcuts import render
from app1.models import *


# Create your views here.
def displaywebpages(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render (request,'displaywebpages.html',d)



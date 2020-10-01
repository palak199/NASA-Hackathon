from django.shortcuts import render
from .models import orgs,ngos
# Create your views here.

def orgs_view(request):
    contents=orgs.objects.all()
    return render(request,'orgs.html',{'contents':contents})

def ngos_view(request):
    contents=ngos.objects.all()
    return render(request,'ngos.html',{'contents':contents})
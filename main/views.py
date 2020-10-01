from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request, 'index.html')

def tables(request):
    return render(request,'tables.html')
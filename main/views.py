from django.shortcuts import render
import random
# Create your views here.
from django.shortcuts import render
import random
from bs4 import BeautifulSoup
import requests
from .models import Water_level
import datetime
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    source = requests.get('http://124.253.142.66').text
    soup=BeautifulSoup(source,'lxml')
    match=soup.p.text
    
    context = {
        
        'data':match
    }

    try :
        user=request.user
        if user:
            today = datetime.datetime.now().date()
            x=Water_level.objects.filter(user=request.user).first()

            if x :
                y=x.time.date()
                if y==today:
                    return render(request,'index.html',context)
                else:
                    new=Water_level.objects.create(user=request.user)
                    new.save()
            else:
                new=Water_level.objects.create(user=request.user)
                new.save()
            
            return render(request, 'index.html',context)
    except:
        return render(request, 'index.html')

        

def survey(request):
    return render(request,'survey-individual.html')   
def leaderboard(request):
    return render(request,'leaderboard.html')
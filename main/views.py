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
    tips=["Put on an extra layer of clothing instead of turning on the heating. Seriously doubling up on your socks does wonders!","Open up your blinds and use as much natural light as possible before switching on your light bulbs. You all get to enjoy some more sunshine",
       "Turn off your lights when you leave a room.",
       "Put up a no junk mail sign on your letterbox to limit the amount of paper waste.","Hang your wet clothes on a drying line or rack instead of using a powered dryer","Hand wash your clothes particularly if you only have a few items to clean.",
       "Start timing your showers. Or invest in a shower timer","Grow your own herbs, fruit and vegetables even if it’s just a few pots around the house, it all helps!",
       "Turn off your devices at night including your wifi box.",
       "Get a water-saving showerhead.”,“Use organic fertilisers.",
       "Purchase recycled toilet paper with plastic-free packaging.",
       "On the topic of toilets use scrap paper or newspaper or toilet paper to collect pet poo."]

    source = requests.get('http://124.253.142.66').text
    soup=BeautifulSoup(source,'lxml')
    match=soup.p.text
    
    context = {
        
        'tip': random.choice(tips),
        'data':match
    }

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

def survey(request):
    return render(request,'survey-individual.html')   
def leaderboard(request):
    return render(request,'leaderboard.html')
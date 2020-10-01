from django.shortcuts import render
import random
# Create your views here.
def index(request):
    tips=["Put on an extra layer of clothing instead of turning on the heating. Seriously doubling up on your socks does wonders!","Open up your blinds and use as much natural light as possible before switching on your light bulbs. You all get to enjoy some more sunshine",
       "Turn off your lights when you leave a room.",
       "Put up a no junk mail sign on your letterbox to limit the amount of paper waste.","Hang your wet clothes on a drying line or rack instead of using a powered dryer","Hand wash your clothes particularly if you only have a few items to clean.",
       "Start timing your showers. Or invest in a shower timer","Grow your own herbs, fruit and vegetables even if it’s just a few pots around the house, it all helps!",
       "Turn off your devices at night including your wifi box.",
       "Get a water-saving showerhead.","Use organic fertilisers.",
       "Purchase recycled toilet paper with plastic-free packaging.",
       "On the topic of toilets use scrap paper or newspaper or toilet paper to collect pet poo."]

    
    context = {
        
        'tip': random.choice(tips),
        
    }
    return render(request, 'index.html',context)

def tables(request):
    return render(request,'tables.html')
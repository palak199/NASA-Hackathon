from django.shortcuts import render
import random
# Create your views here.
def index(request):
  
    return render(request, 'index.html')

def survey(request):
    return render(request,'survey-individual.html')   

def leaderboard(request):
    return render(request,'leaderboard.html')
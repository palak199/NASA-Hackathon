from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Carbon_footprint
import datetime




# Create your views here.
def c_footprint(request):
    date        =  datetime.datetime.now().strftime("%x")
    check=Carbon_footprint.objects.all().filter(user=request.user)
    if check:
        check=check[0].date.strftime("%x")
        if check==date:
            return render(request,'404.html')
    print(check)
    if request.method=='POST':
        x=Carbon_footprint.objects.create(
            user=request.user,
            electric= request.POST["electric"], 
            gas=request.POST["gas"],
            oil=request.POST["oil"],
            car=request.POST["car"],
            flights=request.POST["flights"],
            newspaper=request.POST["newspaperOptionsRadios"],
            aluminium=request.POST["alumtinOptionsRadios"],
        )
        x.save()

        return redirect('home')
    return render(request , 'carbon_footprint.html')
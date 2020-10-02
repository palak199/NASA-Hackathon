


from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.contrib import messages
from django.template.loader import render_to_string
import smtplib 
from sustain.settings import EMAIL_HOST_USER
from django.core.mail import send_mail



# Create your views here.
def send_pledge(request):
    
    if request.method == 'POST':
        subject = "Pledge signed"
        plain_message="Congrats."
        message = render_to_string('pledge-signed.html')
        message.content_subtype = "html"
        recievers = []
        user=request.user
       
        recievers.append(user)
        
        
        send_mail(subject, plain_message, EMAIL_HOST_USER, recievers,html_message=message)
        return redirect('home')
    
    else:
        redirect('survey')


   
        
    



   
            


  
  


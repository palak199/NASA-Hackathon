from django.db import models
from tinymce.models import HTMLField

Trend_CHOICES = (
   ('Y', 'Yes'),
   ('N', 'No')
)

class Blog (models.Model):
    
    name         = models.CharField(max_length=50)
    content      = HTMLField()
    author       = models.CharField(max_length=20) 
    trends       = models.CharField(choices=Trend_CHOICES, max_length=128)
    category     = models.CharField(max_length=20)
    images       = models.ImageField(upload_to= 'images/blog',default='')
    description  = models.TextField(max_length=250)


    def __str__(self):
        return self.name 

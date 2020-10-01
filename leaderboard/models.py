from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Indus_lb(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    score               = models.IntegerField()
    class Meta:
        ordering = ['-score']


class Indv_lb(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    score               = models.IntegerField()
    class Meta:
        ordering = ['-score']


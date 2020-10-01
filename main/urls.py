from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home' ),
    path('table',views.tables,name='table')                #only for getting the map
    
]
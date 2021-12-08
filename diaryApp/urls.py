from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('record', views.register_milk, name='register_milk'),
    
]
from django.shortcuts import render, redirect
from .models import Farmer, Milk

# Create your views here.

def index(request):
    farmer = Farmer.objects.all()

    if request.method == 'POST':
        new_farmer = Farmer(
            names = request.POST['names'],
            phone = request.POST['phone'],
            village = request.POST['village'],
            nin = request.POST['nin'],
            cows = request.POST['cows']
        )
        new_farmer.save()
        return redirect('/')

    return render(request, "index.html",{'farmers':farmer})


def register_milk(request):
    milk = Milk.objects.all()

    if request.method == 'POST':
        delivered_milk = Milk (
            # farmer = request.POST['farmerName'],
            date = request.POST['date'],
            time = request.POST['time'],
            amount = request.POST['amount'],
            # taste = request.POST['taste'],
            # smell = request.POST['smell'],
            # delivery = request.POST['delivery'],
            # adulteration = request.POST['adulteration']
        )
        delivered_milk.save()
        return redirect('/')

    return render(request, "milk2.html",{'dmilk':milk})



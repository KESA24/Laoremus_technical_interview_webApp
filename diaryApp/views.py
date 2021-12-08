from django.shortcuts import render, redirect
from .models import Farmer
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


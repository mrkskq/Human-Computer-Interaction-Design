from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    travels = Travel.objects.all()
    context = {"travels" : travels}
    return render(request, 'index.html', context)

def add(request):
    if request.method == "POST":
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.guide = TouristGuide.objects.get(user = request.user)
            travel.save()
            return redirect('index')
    form = TravelForm
    context = {"form" : form}
    return render(request, 'add.html', context)
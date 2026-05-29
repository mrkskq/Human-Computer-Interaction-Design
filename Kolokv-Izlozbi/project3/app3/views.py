from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    all_exhibitions = Exhibition.objects.all()
    context = {"exhibitions" : all_exhibitions}
    return render(request, 'index.html', context)

def add(request):
    if request.method == "POST":
        form = ExhibitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ExhibitionForm()
    context = {"form" : form}
    return render(request, 'add.html', context)

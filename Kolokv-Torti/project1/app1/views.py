from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    cakes = Cake.objects.all()
    context = {"cakes" : cakes}
    return render(request, 'index.html', context)

def add(request):
    if request.method == "POST":
        form = CakeForm (request.POST, request.FILES)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.baker = Baker.objects.get(user = request.user)
            cake.save()
            return redirect('index')
    form = CakeForm()
    context = {"form": form}
    return render(request, 'add.html', context)

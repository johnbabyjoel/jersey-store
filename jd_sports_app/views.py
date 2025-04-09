from django.shortcuts import render, redirect
from .models import Jersey
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

def index(request):
    jerseys = Jersey.objects.all()
    return render(request, 'index.html', {'jerseys': jerseys})


from django.shortcuts import render, redirect
from .models import Jersey
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

def index(request):
    jerseys = Jersey.objects.all()
    return render(request, 'index.html', {'jerseys': jerseys})

def add_jersey(request):
    if request.method == 'POST':
        name = request.POST['name']
        team = request.POST['team']
        size = request.POST['size']
        price = request.POST['price']
        stock = request.POST['stock']
        image = request.FILES.get('image')  # use request.FILES

        Jersey.objects.create(
            name=name,
            team=team,
            size=size,
            price=price,
            stock=stock,
            image=image
        )
        return redirect('/')
    return render(request, 'create.html')


    
def delete_jersey(request, jersey_id):
    try:
        jersey = Jersey.objects.get(id=jersey_id)
        jersey.delete()
    except Jersey.DoesNotExist:
        pass
    return redirect('/')
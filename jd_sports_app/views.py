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

def edit_jersey(request, id):
    jersey = get_object_or_404(Jersey, pk=id)

    if request.method == "POST":
        jersey.name = request.POST.get('name')
        jersey.team = request.POST.get('team')
        jersey.size = request.POST.get('size')
        jersey.price = request.POST.get('price')
        jersey.stock = request.POST.get('stock')

        if 'image' in request.FILES:
            jersey.image = request.FILES['image']

        jersey.save()
        messages.success(request, "Jersey updated successfully.")
        return redirect('jersey_list')

    return render(request, 'edit_jersey.html', {'jersey': jersey})
    
def delete_jersey(request, jersey_id):
    try:
        jersey = Jersey.objects.get(id=jersey_id)
        jersey.delete()
    except Jersey.DoesNotExist:
        pass
    return redirect('/')
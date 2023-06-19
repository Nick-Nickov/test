from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from .models import Depo, Driver, Transport
from django.shortcuts import render
from .models import Trolleybus
from django.shortcuts import render, get_object_or_404

def index(request):
    depo_list = Depo.objects.all()
    context = {'depo_list': depo_list}
    return render(request, 'depo_app/index.html', context)

def depo_detail(request, depo_id):
    depo = get_object_or_404(Depo, pk=depo_id)
    return render(request, 'depo_app/depo_detail.html', {'depo': depo})

def trolleybuses(request):
    trolleybuses = Trolleybus.objects.all()
    return render(request, 'depo/trolleybuses.html', {'trolleybuses': trolleybuses})

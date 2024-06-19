from django.shortcuts import render
from .models import Handbag

def handbag_list(request):
    handbags = Handbag.objects.all()
    return render(request, 'handbag_list.html', {'handbags': handbags})

def handbag_detail(request, pk):
    handbag = Handbag.objects.get(pk=pk)
    return render(request, 'handbag_detail.html', {'handbag': handbag})
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MaterialMasterForm

# Create your views here.
def index(request):
    return render(request,'ProductMaster/index.html')

def other(request):
    return HttpResponse('This is other page')


def MaterialMasterView(request):
    if request.method == 'POST':
        form = MaterialMasterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MaterialMasterForm()
    return render(request, 'ProductMaster/material_master.html', {'form': form})

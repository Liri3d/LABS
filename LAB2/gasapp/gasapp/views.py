from django.shortcuts import render, redirect
from .models import GasReading
from .forms import GasReadingForm

def index(request):
    readings = GasReading.objects.all()
    return render(request, 'index.html', {'readings': readings})

def add_reading(request):
    if request.method == 'POST':
        form = GasReadingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GasReadingForm()
    return render(request, 'add.html', {'form': form})

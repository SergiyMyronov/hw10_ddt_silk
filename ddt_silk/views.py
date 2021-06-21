from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CityForm
from .models import City


def index(request):
    return HttpResponse("Hello, world. You're at the ddt_silk index.")


def city(request):
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(city)
    else:
        form = CityForm

    return render(request, 'ddt_silk/city.html', {'form': form, 'cities': cities})


def city_update(request, city_id):
    c = get_object_or_404(City, pk=int(city_id))
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST, instance=c)
        if form.is_valid():
            form.save()
            return redirect(city)
    else:
        form = CityForm(instance=c)

    return render(request, 'ddt_silk/city.html', {'form': form, 'cities': cities})

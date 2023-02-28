from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Car


# Create your views here.
def index(request):
    return HttpResponse('Welcome')

def cars(request):
    cars_list = Car.objects.all()
    return render(request, "all_cars.html", {"cars": cars_list})

def car_details(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, "car_details.html", {"car": car})

def car_add(request):
    car_data = request.POST.dict()
    try:
        car = Car(
            name = car_data["name"],
            year = car_data["year"],
            model = car_data["model"],
            fuel = car_data["fuel"]
        )
        car.save()
    except KeyError:
        return render(request, "error.html", {"error_message":"Error!"})
    return HttpResponseRedirect(reverse("cars:all_cars"))
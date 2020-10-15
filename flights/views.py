from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from .models import  Airport, Flight, Passenger

# Create your views here.

def home(request):
    return render(request, "flights/home.html")


def travel(request):
        return render(request, "flights/travel.html", context={"flights": Flight.objects.all()})


def flight(request, flight_id):

    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", context = {"message": "Flight Doesn't Exist!"})

    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
    }
    return render(request, "flights/flight.html", context)


def flights(request):
    try:
        flights = Flight.objects.all()
    except Flight.DoesNotExist:
        return render(request, "error.html", context={"message": "Flight Does Not Exist!!"})

    return render(request, "flights/flights.html", context = {"flights": flights})


def book(request):
    try:
        flight_id  = int(request.POST.get("flight_id"))
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, "flights/error.html", context={"message": "KeyError!!"})
    except Flight.DoesNotExist:
        return Http404("Flight Doesn't Exist!!")

    try:
        first = str(request.POST.get("first"))
    except KeyError:
        return render(request, "flights/error.html", context={"message": "KeyError!!"})

    try:
        last = str(request.POST.get("last"))
    except KeyError:
        return render(request, "flights/error.html", context={"message": "KeyError!!"})

    try:
        age = int(request.POST.get("age"))
    except KeyError:
        return render(request, "flights/error.html", context={"message": "KeyError!!"})

    try:
        email = str(request.POST.get("email"))
    except KeyError:
        return render(request, "flights/error.html", context={"message": "KeyError!!"})

    try:
        sex = str(request.POST.get("sex"))
    except KeyError:
        return render(request, "flights/error.html", context={"message": "KeyError!!"})

    sex = sex[0]

    p = Passenger.objects.filter(first=first, last=last, age=age, email=email, sex=sex)

    if not p:
        p = Passenger(first=first, last=last, age=age, email=email, sex=sex)
        p.save()
        p.flights.add(flight)
        p.save()

    elif p not in flight.passengers.all():
        p = Passenger.objects.get(first=first, last=last, age=age, email=email, sex=sex)
        p.flights.add(flight)
        p.save()

    else:
        return render(request, "flights/error.html", context={"message": "Already Onboard!", "id": id})

    return HttpResponseRedirect(reverse("flight", args=(flight_id, )))

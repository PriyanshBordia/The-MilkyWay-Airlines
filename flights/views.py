from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout

from django.core.mail import send_mail

from .models import  Airport, Flight, Passenger, Food, Ticket

# Create your views here.

def home(request):
    return render(request, "flights/home.html")


def travel(request):
        return render(request, "flights/travel.html", context={"flights": Flight.objects.all(), "foods": Food.objects.all()})


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
        return render(request, "flights/error.html", context={"message": "Flight Does Not Exist!!", "type": "DoesNotExist.!!"})

    return render(request, "flights/flights.html", context = {"flights": flights})


def book(request):

    try:
        flight_id  = int(request.POST.get("flight_id"))
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, "flights/error.html", context={"message": "Enter a Flight Id!!", "type": "Key Error!!"})
    except Flight.DoesNotExist:
        return Http404("Flight Doesn't Exist!!")


    try:
        first = str(request.POST.get("first"))
    except KeyError:
        return render(request, "flights/error.html", context={"message":  "Enter a First Name!!", "type": "Key Error!!"})
    except ValueError:
        return render(request, "flights/error.html", context={"message": "Invalid Value to given field!!", "type": "Value Error!!"})
    except TypeError:
        return render(request, "flights/error.html", context={"message": "Incompatible DataType!!", "type": "Type Error!!",})

    try:
        last = str(request.POST.get("last"))
    except KeyError:
        return render(request, "flights/error.html", context={"message":  "Enter a Last Name!!", "type": "Key Error!!"})
    except ValueError:
        return render(request, "flights/error.html", context={"message": "Invalid Value to given field!!", "type": "Value Error!!"})
    except TypeError:
        return render(request, "flights/error.html", context={"message": "Incompatible DataType!!", "type": "Type Error!!",})

    try:
        age = int(request.POST.get("age"))
    except KeyError:
        return render(request, "flights/error.html", context={"message": "Enter a Age!", "type":"Key Error!!"})
    except ValueError:
        return render(request, "flights/error.html", context={"message": "Invalid Value to given field!!", "type": "Value Error!!"})
    except TypeError:
        return render(request, "flights/error.html", context={"message": "Incompatible DataType!!", "type": "Type Error!!",})

    try:
        email = str(request.POST.get("email"))
    except KeyError:
        return render(request, "flights/error.html", context={"message": "Enter a e-mail address!!", "type": "KeyError!!"})
    except ValueError:
        return render(request, "flights/error.html", context={"message": "Invalid Value to given field!!", "type": "Value Error!!"})
    except TypeError:
        return render(request, "flights/error.html", context={"message": "Incompatible DataType!!", "type": "Type Error!!",})

    try:
        sex = str(request.POST.get("sex"))
    except KeyError:
        return render(request, "flights/error.html", context={"message": "Select appropriate gender from the options provided.!!", "type": "KeyError!!"})

    sex = sex[0]

    p = Passenger.objects.filter(first=first, last=last, age=age, email=email, sex=sex)

    if not p:
        p = Passenger(first=first, last=last, age=age, email=email, pn_no="0000000", sex=sex)
        p.save()
        p.flights.add(flight)
        p.save()

    elif p not in flight.passengers.all():
        p = Passenger.objects.get(first=first, last=last, age=age, email=email, pn_no="0000000", sex=sex)
        p.flights.add(flight)
        p.save()

    else:
        return render(request, "flights/error.html", context={"message": "Already Onboard!", "type": "Hello.!"})

    return HttpResponseRedirect(reverse("flight", args=(flight_id, )))


def user(request, p_id):
    try:
        user_details = Passenger.objects.get(pk=p_id)
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", context = {"message": "Flight Doesn't Exist!", "type": "Value DoesNotExist.!!", })

    return render(request, "flights/user.html", context = {"user_details"})


def reset(request, p_id):
    send_mail(
    'Password Reset Link',
    'Hello.!, there below is the link where you can reset your password.',
    '19ucs257@lnmiit.ac.in',
    ['to@example.com'],
    fail_silently=False,
# )

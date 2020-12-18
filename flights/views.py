from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout

from django.core.mail import send_mail

from .models import  Airport, Flight, Passenger, Food, Ticket
from .forms import ImageForm
# Create your views here.

def home(request):
    return render(request, "flights/home.html")


def travel(request):
        return render(request, "flights/travel.html", context={"flights": Flight.objects.all(), "foods": Food.objects.all()})


def flight(request, flight_id):

    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", context = {"message": "Flight Doesn't Exist!", "type": "DoesNotExist.!!"})

    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
    }
    return render(request, "flights/flight.html", context)


def flights(request):
    try:
        flights = Flight.objects.all()
    except:
        return render(request, "flights/error.html", context={"message": "Flights Does not exists!!", "type": "Does Not exists.!!"})

    if (len(flights) == 0):
        return render(request, "flights/success.html", context={"message": "NO Flights!!", "type": "Empty Set.!!"})

    return render(request, "flights/flights.html", context = {"flights": flights})


def passengers(request):
    try:
        passengers = Passenger.objects.all()
    except:
        return render(request, "flights/error.html", context={"message": "Passengers Do not exists!!", "type": "Does Not exists..!!"})

    if (len(passengers) == 0):
        return render(request, "flights/success.html", context={"message": "NO Passengers!!", "type": "Empty Set.!!"})

    return render(request, "flights/passengers.html", context = {"passengers": passengers})


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

    try:
        origin_date = str(request.POST.get("origin_date"))
    except KeyError:
        return render(request, "flights/error.html", context={"message": "Select a valid date.!!", "type": "KeyError!!"})

    try:
        origin_date = str(request.POST.get("destination_date"))
    except KeyError:
        return render(request, "flights/error.html", context={"message": "Select a valid date.!!", "type": "KeyError!!"})

    p = Passenger.objects.filter(first=first, last=last, age=age, email=email, sex=sex)
    f = Flight.objects.filter()

    if not p:
        p = Passenger(first=first, last=last, age=age, email=email, ph_no=ph_no, sex=sex)
        p.save()
        p.flights.add(flight)
        p.save()

    elif p not in flight.passengers.all():
        p = Passenger.objects.get(first=first, last=last, age=age, email=email, ph_no=ph_no, sex=sex)
        p.flights.add(flight)
        p.save()

    else:
        return render(request, "flights/error.html", context={"message": "Already Onboard!", "type": "Hello.!"})

    return HttpResponseRedirect(reverse("flight", args=(flight_id, )))


def user(request, user_id):

    try:
        user_details = Passenger.objects.get(pk=user_id)
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", context = {"message": "PAssenger Doesn't Exist!", "type": "Value DoesNotExist.!!", })

    return render(request, "flights/user.html", context = {"user_details"})


def reset(request):

    return render(request, "registration/password_reset_form.html", context = {})


def resetLink(request):

    send_mail(
    'Password Reset Link',
    'Hello.!, there below is the link where you can reset your password.',
    '19ucs257@lnmiit.ac.in',
    '19uec117@lnmiit.ac.in',
    fail_silently=False,
)

def imgUpload(request):
     """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

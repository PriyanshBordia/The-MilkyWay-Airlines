from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
import datetime

# Create your models here.

class Airport(models.Model):

    code = models.CharField(max_length=3, blank=False, null=False)
    city = models.CharField(max_length=64, blank=False, null=False)
    country = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return f"({self.code}) {self.city}, {self.country}"

    def is_valid_airport(self):
        return (len(self.code) > 0 and len(self.city) > 0 and len(self.country) > 0)
    
    # class Meta:
    #     db_table = 'Airport'
    #     managed = False


class Flight(models.Model):

    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")

    origin_date = models.DateTimeField(blank=False, null=False, default=timezone.now)
    destination_date = models.DateTimeField(blank=False, null=False, default=timezone.now)

    duration = models.IntegerField(validators=[MinValueValidator(1)], blank=False, null=False, default=1)

    capacity = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True, default=1)

    def __str__(self):
        return f"{self.origin} to {self.destination}, in {self.duration} mins."

    def is_valid_flight(self):
        return ((self.origin != self.destination) and (self.duration > 0) and (self.origin_date < self.destination_date))

    # class Meta:
    #     db_table = 'Flight'
    #     managed = False

class Food(models.Model):

    price = models.DecimalField(decimal_places=2, max_digits=1000, blank=False, null=False, default=1)
    name = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

    def is_valid_food(self):
        return (self.price > 0 and len(self.name) > 0)
    
    # class Meta:
        # db_table = 'Food'
        # managed = False


class Ticket(models.Model):

    Modes = [('E', 'Economy Class'), ('B', 'Bussiness Class'), ('A', 'First Class'),]
    Types = [('A', 'Aisle'), ('M', 'Middle'), ('W', 'Window'), ]

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="flight")

    hospitality = models.CharField(max_length=1, choices=Modes, blank=False, null=False)
    seat = models.CharField(max_length=1, choices=Types, blank=False, null=False, default='M')

    price = models.FloatField(validators=[MinValueValidator(1)], blank=False, null=False)
    food = models.ManyToManyField(Food, related_name="cuisines", blank=True)

    booking_date = models.DateTimeField(blank=False, null=False, default=timezone.now)

    def __str__(self):
        return f"{self.hospitality}{self.seat}{self.id}"
    
    # class Meta:
        # db_table = 'Ticket'
        # managed = False


class Passenger(models.Model):

    options = (('M', 'Male'), ('F', 'Female'), ('X', 'Not Preferred to say'),)

    first = models.CharField(max_length=21, blank=False, null=False)
    last = models.CharField(max_length=21, blank=False, null=False)

    age = models.IntegerField(validators=[MinValueValidator(1)], blank=False, null=False, default=1)
    sex = models.CharField(max_length=1, choices=options, blank=False, null=False, default='X')

    email = models.EmailField(blank=False, null=False)
    ph_no = models.BigIntegerField(blank=True, null=False, default=0000000)

    flights = models.ManyToManyField(Flight, related_name="passengers", blank=True)

    tickets = models.ManyToManyField(Ticket, related_name="journeys", blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return f"{self.first} {self.last}  {self.sex} {self.age}"

    def is_valid_passenger(self):
        return (self.age > 0 and len(self.first) > 0)
    
    # class Meta:
        # db_table = 'Passenger'
        # managed = False


class Cancel(models.Model):

    ticketId = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="cancellation", blank=False, null=False)

    def __str__(self):
        return f"{self.ticketID}"

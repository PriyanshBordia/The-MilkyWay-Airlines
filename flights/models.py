from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Airport(models.Model):

    code = models.CharField(max_length=3, blank=False, null=False)
    city = models.CharField(max_length=64, blank=False, null=False)
    country = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return f"({self.code}) {self.city}, {self.country}"


class Flight(models.Model):

    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")

    origin_date = models.DateTimeField(blank=False, null=False)
    destination_date = models.DateTimeField(blank=False, null=False)

    duration = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.origin} to {self.destination}, in {self.duration} mins."

    def is_valid_flight(self):
        return ((self.origin != self.destination) and (self.duration > 0) and (self.origin_date < self.destination_date))


class Food(models.Model):

    price = models.DecimalField(decimal_places=2, max_digits=1000, blank=False, null=False, default=1)
    name = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"


class Ticket(models.Model):

    Modes = [('E', 'Economy Class'), ('B', 'Bussiness Class'), ('A', 'First Class'),]
    Types = [('A', 'Aisle'), ('M', 'Middle'), ('W', 'Window'), ]

    hospitality = models.CharField(max_length=1, choices=Modes, blank=False, null=False)
    seat = models.CharField(max_length=1, choices=Types, blank=False, null=False, default='M')

    price = models.FloatField(validators=[MinValueValidator(1)], blank=False, null=False)
    food = models.ManyToManyField(Food, related_name="cusines", blank=True)

    def __str__(self):
        return f"{self.hospitality}{self.seat}{self.id}"


class Passenger(models.Model):

    options = (('M', 'Male'), ('F', 'Female'), ('X', 'Not Prefered to say'),)

    first = models.CharField(max_length=21, blank=False, null=False)
    last = models.CharField(max_length=21, blank=False, null=False)

    age = models.IntegerField(validators=[MinValueValidator(1)], blank=False, null=False, default=1)
    sex = models.CharField(max_length=1, choices=options, blank=False, null=False, default='X')

    email = models.EmailField(blank=False, null=False, default='user@mail.co')
    ph_no = models.BigIntegerField(blank=True, null=True)

    flights = models.ManyToManyField(Flight, related_name="passengers", blank=True)
    tickets = models.ManyToManyField(Ticket, related_name="journeys", blank=True)

    def __str__(self):
        return f"{self.first} {self.last}"

    def is_valid_passenger(self):
        return (self.age > 0 and len(self.first) > 0)

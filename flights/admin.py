from django.contrib import admin

from .models import Airport, Flight, Passenger, Food, Ticket, Cancel

class PassengerInline(admin.StackedInline):
    model = Passenger.flights.through
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]

# class FoodInline(admin.StackedInline):
#     model = Food.
#     inlines = []

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger)
admin.site.register(Food)
admin.site.register(Ticket)
admin.site.register(Cancel)


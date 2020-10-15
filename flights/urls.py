from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("travel", views.travel, name="travel"),
    path("flight/<int:flight_id>", views.flight, name="flight"),
    path("flights", views.flights, name="flights"),
    path("book", views.book, name="book"),
]

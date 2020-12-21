from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("travel", views.travel, name="travel"),
    path("book", views.book, name="book"),
    path("flight/<int:flight_id>", views.flight, name="flight"),
    path("flights", views.flights, name="flights"),
    path("passenger/<int:p_id>", views.passengers, name="passenger"),
    path("passengers", views.passengers, name="passengers"),
    path("user", views.user, name="user"),
    path("user", views.user, name="users"),
    path("reset", views.reset, name="reset"),
    path("resetLink", views.resetLink, name="resetLink"),
]

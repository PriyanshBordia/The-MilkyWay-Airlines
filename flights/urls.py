from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("travel", views.travel, name="travel"),
    path("book", views.book, name="book"),
    path("bookid/<int:p_id>", views.bookid, name="bookid"),
    path("flight/<int:flight_id>", views.flight, name="flight"),
    path("flights", views.flights, name="flights"),
    path("passenger/<int:p_id>", views.passenger, name="passenger"),
    path("passengers", views.passengers, name="passengers"),
    path("user", views.user, name="user"),
    path("users", views.users, name="users"),
    path("userid/<int:user_id>", views.userid, name="userid"),
    path("update", views.update, name="update"),
    path("resetLink", views.resetLink, name="resetLink"),
]

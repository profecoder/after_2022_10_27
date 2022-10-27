from django.urls import path

from my_app import views

app_name = "my_app"
urlpatterns = [
    path("cars", view=views.cars, name="car-list"),
    path("car/add", view=views.create_cars, name="car-add"),
]

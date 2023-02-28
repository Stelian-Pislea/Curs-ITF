from django.urls import path
from . import views
app_name = "cars"
urlpatterns = [
    path("", views.cars, name="all_cars"),
    path("<int:car_id>/", views.car_details, name="car_details"),
    path("car/", views.car_add, name="add")
]
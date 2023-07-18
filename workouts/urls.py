from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.index),
    path("<int:day>", views.workout_by_day_in_number),
    path("<str:day>", views.workout, name="day-workout")
]
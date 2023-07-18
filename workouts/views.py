from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
# Create your views here.

days = {
    "sunday": "Biceps",
    "monday": "Legs",
    "tuesday": "Shoulders",
    "wednesday": "Thighs",
    "thursday": "Back",
    "friday": "Abs",
    "saturday": "Triceps"
}

def index(request):
    list_items = ""
    for day in days:
        capitalized_day = day.capitalize()
        response_path = reverse("day-workout", args=[day])
        list_items += f"<li><a href=\"{response_path}\">{capitalized_day}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def workout_by_day_in_number(request, day):
    days_list = list(days.keys())
    redirect_day = days_list[day - 1]
    redirect_path = reverse("day-workout", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)
#   return HttpResponseRedirect("/workouts/" + redirect_day)

def workout(request, day):
    try:
        workout_text = days[day]
        response_data = f"<h1>{workout_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This day is not supported</h1>")
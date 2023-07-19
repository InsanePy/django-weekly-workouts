from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
# Create your views here.

days = {
    "sunday": "Biceps",
    "monday": "Legs",
    "tuesday": "Shoulders",
    "wednesday": "Thighs",
    "thursday": "Back",
    "friday": "Abs",
    "saturday": None
}


def index(request):
    days_list = list(days.keys())
    return render(request, "workouts/index.html", {
        "days_list": days_list
    })

def workout_by_day_in_number(request, day):
    days_list = list(days.keys())
    redirect_day = days_list[day - 1]
    redirect_path = reverse("day-workout", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)
#   return HttpResponseRedirect("/workouts/" + redirect_day)


def workout(request, day):
    try:
        workout_text = days[day]
        return render(request, "workouts/workout.html", {
            "day": day,
            "workout_text": workout_text
        })
    except:
        raise Http404()
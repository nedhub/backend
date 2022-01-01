from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def january(request):
    return HttpResponse("This works!")



def feburary(request):
    return HttpResponse("Walk for at least 20 mins every day!")


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat no meat for the entire month!"

    elif month == 'february':
        challenge_text = "Walk for at least 20 mins everyday"

    elif month == "march":
        challenge_text = "Learn Django for at least 20 mins every day!"

    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
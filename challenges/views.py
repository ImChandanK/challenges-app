from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here


def monthly_challenge(request, month):

    mappings = {
        'january': 'The reign of Lucifer starts',
        'february': "I'm gonna conquer the world",
        'march': 'We reached march',
        'april': 'We reached april',
        'may': 'We reached may'
    }

    try:
        return HttpResponse(mappings[month])
    except KeyError:
        return HttpResponseNotFound("This Month is not found")

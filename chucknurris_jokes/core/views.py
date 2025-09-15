from django.http import HttpResponse
import requests

# Create your views here.

def do_a_request():
    URL = "https://api.adviceslip.com/advice"
    req = requests.get(URL)
    response = req.json()
    return response["slip"]["advice"]

def chucknurris(request):
    return HttpResponse(do_a_request())
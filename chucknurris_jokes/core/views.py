import requests
from django.shortcuts import render

def do_a_request():
    URL = 'https://api.chucknorris.io/jokes/random'
    req = requests.get(URL)
    dados_recebidos = req.json()
    return dados_recebidos

# Create your views here.
def chuck(request):
    response = do_a_request()
    return render(request, 'chucknorris.html', response)
from pprint import pprint
from django.shortcuts import render
import requests
from pprint import pprint
import random

# Create your views here.
def index(request):
    card = list(range(8))
    BASE_URL = ''
    return render(request, 'movies/index.html')

def recommendations(request):
    return render(request, 'movies/recommendations.html')
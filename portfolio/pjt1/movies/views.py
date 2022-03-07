from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')

def recommendations(request):
    return render(request, 'movies/recommendations.html')
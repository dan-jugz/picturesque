from django.shortcuts import render,redirect,Http404
from .models import Image,Category,Location

# Create your views here.

def home(request):
    images = Image.display_images()
    locations = Location.display_locations()
    return render (request,'home.html',{"images":images,"locations":locations})


def search_results(request):
    search = request.GET.get('searched_category')
    searched_images = Image.search_category(search)
    message = f'{search}'
    return render (request,'searched.html',{"images":searched_images,"message":message})

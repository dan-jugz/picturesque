from django.shortcuts import render,redirect,Http404
from .models import Image,Category,Location

# Create your views here.

def home(request):
    images = Image.display_images()
    locations = Location.display_locations()
    return render (request,'home.html',{"images":images,"locations":locations})



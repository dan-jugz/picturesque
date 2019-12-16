from django.shortcuts import render,redirect,Http404
from .models import Image,Category,Location

# Create your views here.

def home(request):
    images = Image.display_images()
    locations = Location.display_locations()
    return render (request,'home.html',{"images":images,"locations":locations})


def search_results(request):
    if 'searched_category' in request.GET and request.GET["searched_category"]:
        search = request.GET.get('searched_category')
        searched_images = Image.search_category(search)
        message = f'{search}'
        return render (request,'searched.html',{"images":searched_images,"message":message})
    else:
        message = "You haven't searched for any term"
        return render (request,'searched.html',{"message":message})



def fullimage(request,image_id):
    try:
        the_image = Image.objects.get(id = image_id)
    except DoesNotExist:
        return Http404
  
    return render(request,'fullimage.html',{"image":the_image})

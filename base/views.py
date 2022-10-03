from django.shortcuts import render
from .models import Room

# Create your views here.




def index(request):
    """ A view to return the index page """

    return render(request, 'base/index.html')


def home(request):
    """ A view to return the home page """
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    """ A view to return the main room  page """
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'base/room.html', context)

from multiprocessing import context
from operator import is_not
#from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout


# Create your views here.
# rooms=[
#     {'id':1, 'name':'Let me learn python'},
#     {'id':2, 'name':'Javascript is calling'},
#     {'id':3, 'name':'Photoshop tutorials'},
#     {'id':4, 'name':'Frontend developer'},
# ]

def LogInPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')  

        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home')
        # else:
        #      messages.error(request, 'User does not exist')  

    context = {}
    return render(request, 'Login_register.html', context)










def home(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)|
                                Q(name__icontains=q)|
                                Q(description__icontains=q))
    room_count = rooms.count()                             
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics':topics, 'room_count':room_count}
    return render(request, 'home.html', context)


def room(request,pk):
    # room =None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room=i
    room = Room.objects.get(id = pk)
    context={'room': room}        
    return render(request, 'room.html', context)

def createRoom(request):
    form= RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'room_form.html', context)    

def updateRoom(request,pk):
    room = Room.objects.get(id = pk)
    form= RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')      
    context = {'form': form}
    return render(request, 'room_form.html', context)  


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'delete.html', {'obj':room})     
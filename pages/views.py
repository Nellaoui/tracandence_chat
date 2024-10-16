from django.shortcuts import render, redirect
from .models import Room, Message
# from django.http import HttpResponse

# def homePageView(request):
#     return render(request, 'hello.html')

def HomeView(requset):
    if requset.method == "POST":
        username = requset.POST["username"]
        room = requset.POST["room"]
        try:
            existing_room = Room.objects.get(room_name__icontains=room)
        except Room.DoesNotExist:
            r = Room.objects.create(room_name=room)
        return redirect("room", room_name=room, username=username) 
    return render(requset, "home.html")


def RoomView(requset, room_name, username):
    existing_room = Room.objects.get(room_name__icontains=room_name)
    get_messages = Message.objects.filter(room=existing_room)
    context = {
        "messages": get_messages,
        "user": username,
        "room_name": existing_room.room_name,
        }
    return render(requset, "room.html", context)
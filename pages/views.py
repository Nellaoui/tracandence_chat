from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


def HomeView(requset):
    if requset.method == "POST":
        username1 = requset.POST["username1"]
        username2 = requset.POST["username2"]

        if (username1 == username2):
                return render(requset, "home.html", {"error": "Please enter different usernames"})
        
        user1, user2 = sorted([username1, username2])

        room, created = Room.objects.get_or_create(user1=user1, user2=user2, defaults={"room_name": f"{user1}_{user2}"})
        return redirect("room", room_name=room.room_name, username=username1)
    return render(requset, "home.html")

    #     room = requset.POST["room"]
    #     try:
    #         existing_room = Room.objects.get(room_name__icontains=room)
    #     except Room.DoesNotExist:
    #         r = Room.objects.create(room_name=room)
    #     return redirect("room", room_name=room, username=username) 
    # return render(requset, "home.html")


def RoomView(requset, room_name, username):
    existing_room = Room.objects.get(room_name__icontains=room_name)
    get_messages = Message.objects.filter(room=existing_room)
    context = {
        "messages": get_messages,
        "user": username,
        "room_name": existing_room.room_name,
        }
    return render(requset, "room.html", context)

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
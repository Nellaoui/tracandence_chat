from django.urls import path
from .views import HomeView , RoomView
from .views import RoomList, MessageList

urlpatterns = [
    path('rooms/', RoomList.as_view(), name="room_list"),
    path('messages/', MessageList.as_view(), name="message_list"),
    path("", HomeView, name="login"),
    path("<str:room_name>/<str:username>/", RoomView, name="room")
]

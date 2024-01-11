from django.urls import path
from .views import functionRooms

users_url = [
    path('create_room', functionRooms.create_room, name='create_room'),
    path('get_rooms', functionRooms.get_rooms, name='get_rooms'),
    path('update_room', functionRooms.update_room, name='update_room'),
    path('delete_room', functionRooms.delete_room, name='delete_room'),
]

urlpatterns = users_url
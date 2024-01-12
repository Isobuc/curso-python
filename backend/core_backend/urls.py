from django.urls import path
from .views import functionRooms
from .views import functionUsers

users_url = [
    path('create_room', functionRooms.create_room, name='create_room'),
    path('get_rooms', functionRooms.get_rooms, name='get_rooms'),
    path('update_room', functionRooms.update_room, name='update_room'),
    path('delete_room', functionRooms.delete_room, name='delete_room'),
    path('create_user', functionUsers.create_user, name='create_user'),
    path('get_users', functionUsers.get_users, name='get_users'),
    path('update_user', functionUsers.update_user, name='update_user'),
    path('delete_user', functionUsers.delete_user, name='delete_user'),
    path('get_user', functionUsers.get_user, name='get_user'),
]

urlpatterns = users_url
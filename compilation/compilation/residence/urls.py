from django.urls import path, include
from .views import find_room_view,upload_room_view,available_rooms_view,match_available_rooms_view,about_us_view

urlpatterns = [
    path('find_room/', find_room_view),
    path('upload_room/', upload_room_view),
    path('available_rooms/', available_rooms_view),
    path('available_rooms/<slug:province>/<slug:location>/<slug:section>/', match_available_rooms_view),
    path('about_us/', about_us_view),   
]

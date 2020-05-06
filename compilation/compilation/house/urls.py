from django.urls import path, include
from .views import find_house_view,upload_house_view,available_houses_view,match_available_houses_view,about_house_view

urlpatterns = [
    path('find_house/', find_house_view),
    path('upload_house/', upload_house_view),
    path('available_houses/', available_houses_view),
    path('available_houses/<slug:province>/<slug:location>/<slug:section>/', match_available_houses_view),
    path('about_us/', about_house_view),
    
]

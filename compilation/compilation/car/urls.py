from django.urls import path, include
from .views import find_car_view,upload_car_view,available_cars_view,match_available_cars_view,about_us_view

urlpatterns = [
    path('find_car/', find_car_view),
    path('upload_car/', upload_car_view),
    path('available_cars/', available_cars_view),
    path('available_cars/<slug:province>/<slug:location>/<slug:section>/', match_available_cars_view),
    path('about_us/', about_us_view),
    
]

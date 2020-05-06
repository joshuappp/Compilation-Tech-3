from django.urls import path, include
from .views import home_view,about_us_view

urlpatterns = [
    path('', home_view),
    path('about_us/', about_us_view),
]

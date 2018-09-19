from django.urls import path
from .views import all_art
urlpatterns = [
    path('r_post/<slug:slug>/',all_art),   
]
from django.urls import path
from .views import register,user_login,logout_i,user_articles

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_i, name='logout'),
    path('dashboard/', user_articles, name='articles')
]
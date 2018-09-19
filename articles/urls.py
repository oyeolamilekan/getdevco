from django.urls import path
from .views import n_index,article_list,articles_detail,new_post,edit_post,delete_post

urlpatterns = [
    path('', n_index, name='index'),
    path('new_post/', new_post, name='new_post'),
    path('articles/', article_list, name='article_list'),
    path('edit_post/<int:id>/', edit_post, name='edit_p'),
    path('delete/<int:id>/', delete_post, name='delete_p'),
    path('article_detail/<int:pk>/', articles_detail, name='articles_d'),
]
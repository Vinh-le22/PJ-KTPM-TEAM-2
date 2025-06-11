from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('categories/', views.category_list, name='category_list'),
    path('category/new/', views.category_create, name='category_create'),
    path('authors/', views.author_list, name='author_list'),
    path('author/new/', views.author_create, name='author_create'),
] 
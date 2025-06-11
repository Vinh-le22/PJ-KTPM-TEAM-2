from django.urls import path
from . import views

urlpatterns = [
    path('', views.borrow_list, name='borrow_list'),
    path('new/<int:book_pk>/', views.borrow_create, name='borrow_create'),
    path('<int:pk>/', views.borrow_detail, name='borrow_detail'),
    path('<int:pk>/return/', views.return_book, name='return_book'),
    path('<int:pk>/approve/', views.borrow_approve, name='borrow_approve'),
    path('<int:pk>/reject/', views.borrow_reject, name='borrow_reject'),
] 
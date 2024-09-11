from django.contrib import admin
from django.urls import path
from .views import register
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.book_list, name='book_list'),
    path('manage/', views.manage_books, name='manage_books'),
    path('remind/', views.remind_users, name='remind_users'),
    path('register/', register, name='register'),

]

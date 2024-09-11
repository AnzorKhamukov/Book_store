from django.contrib import admin
from .models import Book, UserProfile, BookRent

admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(BookRent)

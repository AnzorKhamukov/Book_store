from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Book, BookRent
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def rent_book(request, book_id, duration):
    book = Book.objects.get(id=book_id)
    return redirect('book_list')


def manage_books(request):
    books = Book.objects.all()
    return render(request, 'manage_books.html', {'books': books})


def remind_users(request):
    overdue_rents = BookRent.objects.filter(return_date__lt=timezone.now())
    return render(request, 'remind_users.html', {'overdue_rents': overdue_rents})
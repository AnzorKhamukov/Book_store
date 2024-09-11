from django.db import models
from django.contrib.auth.models import AbstractUser



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    publish_year = models.IntegerField()
    price = models.FloatField()
    is_rented = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rented_books = models.ManyToManyField(Book, through='BookRent', related_name='rented_by')


class BookRent(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rent_duration = models.CharField(max_length=20)
    rent_date = models.DateField()
    return_date = models.DateField()


class CustomUser(AbstractUser):
    pass

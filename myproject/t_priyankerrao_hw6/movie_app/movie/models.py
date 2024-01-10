from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    director = models.CharField(max_length=100, blank=True)
    release_year = models.CharField(max_length=50, blank=True)
    budget = models.CharField(max_length=50, blank=True)
    runtime = models.CharField(max_length=50, blank=True)
    rating = models.CharField(max_length=50, blank=True)
    genre = models.CharField(max_length=50, blank=True)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)

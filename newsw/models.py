from datetime import datetime
import requests
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class News(models.Model):
    title = models.TextField(max_length=70)
    name_news = models.TextField(max_length=60)
    date_news = models.DateField()

    def __str__(self):
        return f'{self.title}'

    def __str__(self):
        return f'{self.name_news}'

    def __str__(self):
        return f'self.title'


class Appointment(models.Model):
    date = models.DateField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(max_length=200)

    message = models.TextField()

    def __str__(self):
        return f'{self.client_name}: {self.message}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed_categories = models.ManyToManyField(Category)
    pass


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.username} - {self.name}"


class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    published_date = models.DateTimeField('date published')
    modified_date = models.DateTimeField('date modified')
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.title}"


class CreatePost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    published_date = models.DateTimeField('date published')
    modified_date = models.DateTimeField('date modified')
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    topic = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic


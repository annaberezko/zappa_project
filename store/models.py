from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=40)


class Book(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

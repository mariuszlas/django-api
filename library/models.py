from django.db import models

class Scores(models.Model):
    username = models.CharField(max_length=500)
    score = models.FloatField()

    def __str__(self):
        return f'{self.username} {self.score}'

class Author(models.Model):
    name = models.CharField(max_length=170)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title} {self.author}'

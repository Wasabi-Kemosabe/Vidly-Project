from django.db import models

# Create your models here.
"""
Field:
    Char (string)
    Int
    Float
    Boolean
"""


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Series(models.Model):
    class Meta():
        verbose_name_plural = 'Series'
    title = models.CharField(max_length=250)
    total_gross = models.IntegerField()
    movie_count = models.IntegerField()
    average_gross = models.IntegerField()
    highest_grossing_film = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    duration_min = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.id) + " | " + str(self.release_year) + " | " + self.title

from django.db import models
from movies.models import Genre, Movie, Series
from tastypie.resources import ModelResource, fields, ALL
from tastypie.authorization import Authorization

# Create your models here.


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        ordering = ["release_year", "title", "price"]
        filtering = {
            "release_year": ALL,
            "price": ALL,
            "title": ALL,
            "in_stock": ALL,
            "duration_min": ALL
        }


class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'
        allowed_method = ['get', 'post', 'put', 'patch', 'delete']
        authorization = Authorization()


"""
Filtering
/api/movies
/api/movies/?price=1.2
/api/movies/?duration_min__gt=120
/api/movies/?release_year__gt=1991
/api/movies/?title__contains=Scream

Ordering
/api/movies/?order_by=release_year
/api/movies/?order_by=-release_year
"""

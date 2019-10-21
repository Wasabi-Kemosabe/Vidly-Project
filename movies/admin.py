from django.contrib import admin
from .models import Genre, Movie, Series

# Register your models here.

# Create classes to customize how admin display models


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title')
    list_display = ('id', 'release_year', 'title', 'genre', 'duration_min')


class SeriesAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title')
    list_display = ('id', 'title', 'total_gross', 'movie_count',
                    'average_gross', 'highest_grossing_film')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Series, SeriesAdmin)

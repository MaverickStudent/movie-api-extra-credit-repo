from django.contrib import admin
from .models import Movie

# Register your models here.


class MovieList(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'rating', 'watchrating')
    list_filter = ('name', 'year', 'rating', 'watchrating')
    search_fields = ('name', 'description', 'watchrating')
    ordering = ['year']


admin.site.register(Movie, MovieList)
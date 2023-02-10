from django.db import models
from django.utils import timezone

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=360)
    year = models.IntegerField(blank=False, null=False)
    rating = models.IntegerField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    website = models.URLField(null=True, help_text='Enter the movie/show URL.')

    WATCHRATING_LIST = {
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
    }
    watchrating = models.CharField(
        max_length=10,
        choices=WATCHRATING_LIST,
        default='G')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

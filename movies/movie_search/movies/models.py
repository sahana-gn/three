#from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4, blank=True)
    plot = models.TextField(blank=True)
    poster = models.URLField(blank=True)
    imdb_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title
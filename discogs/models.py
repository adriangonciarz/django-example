from django.db import models
from django.utils import timezone

ARTIST_COUNTRIES = [
    ('pl', "Poland"),
    ('us', "United States"),
    ('uk', "United Kingdom"),
    ('other', "Other"),
]

ALBUM_GENRES = [
    ('rock', 'Rock'),
    ('jazz', 'Jazz'),
    ('funk', 'Funk'),
    ('blues', 'Blues'),
    ('pop', 'Pop'),
    ('metal', 'Metal \m/'),
    ('other', 'Other'),
]


class Artist(models.Model):
    """A model of an Artist"""
    name = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, choices=ARTIST_COUNTRIES, default=ARTIST_COUNTRIES[-1][0])

    def __str__(self):
        return self.name


class Album(models.Model):
    """A model of an Artist's album"""
    title = models.CharField(max_length=512, null=False)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, choices=ALBUM_GENRES, default=ALBUM_GENRES[-1][0])
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Song(models.Model):
    """A model of a song"""
    title = models.CharField(max_length=512, null=False)
    duration = models.PositiveSmallIntegerField(blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_duration_representation(self):
        """Transforms integer second representation to more pleasant format of HH:MM:ss"""
        hours = int(self.duration / 3600)
        minutes = int(self.duration / 60)
        seconds = self.duration % 60
        return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

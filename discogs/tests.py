from django.test import TestCase
from django.urls import reverse

from .models import Artist, Song, Album


class TestSongs(TestCase):
    def setUp(self):
        slayer = Artist.objects.create(name='Slayer', country='us')
        rib_album = Album.objects.create(title='Reign in Blood', year=1986, genre='metal', artist=slayer)
        Song.objects.create(title='Raining Blood', duration=222, album=rib_album)

    def test_song_duration_representation(self):
        song = Song.objects.get(title='Raining Blood')
        duration_representation = song.get_duration_representation()
        self.assertEquals(duration_representation, '00:03:42')


class TestArtistListView(TestCase):
    def setUp(self):
        Artist.objects.create(name='Deep Purple', country='uk')
        Artist.objects.create(name='Slayer', country='us')

    def test_artist_list_view(self):
        response = self.client.get(reverse('discogs:artist-list'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Deep Purple')
        self.assertTemplateUsed(response, 'discogs/artist_list.html')

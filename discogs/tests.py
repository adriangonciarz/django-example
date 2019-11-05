from django.test import TestCase
from django.urls import reverse

from .models import Artist
from .views import artist_list

class TestArtistListView(TestCase):
    def setUp(self):
        Artist.objects.create(name='Deep Purple', country='uk')
        Artist.objects.create(name='Slayer', country='us')

    def test_artist_list_view(self):
        response = self.client.get(reverse('discogs:artist-list'))
        self.assertContains(response, 'Deep Purple')
        self.assertTemplateUsed(response, 'discogs/artist_list.html')
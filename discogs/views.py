from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DeleteView

from .models import Artist, Song
from .forms import ArtistForm, SongForm


def index_view(request):
    return render(request, "discogs/index.html")


class ArtistList(generic.ListView):
    model = Artist
    context_object_name = 'artists'


class ArtistDetails(generic.DetailView):
    model = Artist


class ArtistNew(generic.CreateView):
    form_class = ArtistForm
    model = Artist
    success_url = reverse_lazy('discogs:artist-list')


class ArtistEdit(generic.UpdateView):
    form_class = ArtistForm
    model = Artist


class ArtistDelete(DeleteView):
    model = Artist
    success_url = 'discogs:artist-list'


class SongList(generic.ListView):
    model = Song
    context_object_name = 'all_songs'


class SongDetails(generic.DetailView):
    model = Song
    fields = ('title', 'duration', 'album')


class SongEdit(generic.FormView):
    form_class = SongForm


class ArtistSongList(generic.ListView):
    model = Artist
    template_name = 'discogs/artist_songs.html'
    context_object_name = 'artist_songs'

    def get_queryset(self):
        return Song.objects.filter(album__artist=self.kwargs['pk'])

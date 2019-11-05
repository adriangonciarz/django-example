from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Artist, Song
from .forms import ArtistForm


def index_view(request):
    return render(request, "discogs/index.html")


def artist_list(request):
    all_artists = Artist.objects.all()
    context = {'all_artists': all_artists}
    return render(request, 'discogs/artist_list.html', context)


def artist_details(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'discogs/artist_details.html', {'artist': artist})


def artist_new(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('discogs:artist-details', artist_id=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'discogs/artist_edit.html', {'form': form})


def artist_edit(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('discogs:artist-details', artist_id=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'discogs/artist_edit.html', {'form': form})

class ArtistSongList(generic.ListView):
    model = Artist
    template_name = 'discogs/artist_songs.html'
    context_object_name = 'artist_songs'

    def get_queryset(self):
        return Song.objects.filter(album__artist=self.kwargs['pk'])

from django.urls import path
from . import views

app_name = 'discogs'
urlpatterns = [
    path('', views.index_view),
    path('artists/', views.ArtistList.as_view(), name='artist-list'),
    path('artists/new/', views.ArtistNew.as_view(), name='artist-new'),
    path('artists/<int:pk>/', views.ArtistDetails.as_view(), name='artist-details'),
    path('artists/<int:pk>/delete', views.ArtistDelete.as_view(), name='artist-delete'),
    path('artists/<int:pk>/edit/', views.ArtistEdit.as_view(), name='artist-edit'),
    path('artists/<int:pk>/songs/', views.ArtistSongList.as_view(), name='artist-songs'),
    path('songs/', views.SongList.as_view(), name='song-list'),
    path('songs/new', views.SongEdit.as_view(), name='song-list'),
    path('songs/<int:pk>', views.SongDetails.as_view(), name='song-details'),
]
from django.urls import path
from . import views

app_name = 'discogs'
urlpatterns = [
    path('', views.index_view),
    path('artists/', views.artist_list, name='artist-list'),
    path('artists/new/', views.artist_new, name='artist-new'),
    path('artists/<int:artist_id>/', views.artist_details, name='artist-details'),
    path('artists/<int:artist_id>/edit/', views.artist_edit, name='artist-edit'),
    path('artists/<int:pk>/songs/', views.ArtistSongList.as_view(), name='artist-songs'),
]
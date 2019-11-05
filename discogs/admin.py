from django.contrib import admin
from .models import Artist, Album, Song


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1


class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album)
admin.site.register(Song)

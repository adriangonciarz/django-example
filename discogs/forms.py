from django import forms

from .models import Artist, Song


class ArtistForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArtistForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['country'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Artist
        fields = ('name', 'country',)


class SongForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['album'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['duration'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Song
        fields = ('title', 'album', 'duration',)

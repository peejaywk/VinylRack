from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Artist, Genre, Recordlabel


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        genre_friendly_names = [(c.id, c.get_friendly_name()) for c in genres]
        
        artists = Artist.objects.all()
        artist_friendly_names = [(c.id, c.get_friendly_name()) for c in artists]

        record_labels = Recordlabel.objects.all()
        record_label_friendly_names = [(c.id, c.get_friendly_name()) for c in record_labels]

        self.fields['genre'].choices = genre_friendly_names
        self.fields['artist'].choices = artist_friendly_names
        self.fields['record_label'].choices = record_label_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = '__all__'

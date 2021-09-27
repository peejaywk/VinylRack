from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Artist, Genre, Recordlabel


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    grading_choices = [
            ('M', 'Mint'),
            ('Ex', 'Excellent'),
            ('Vg', 'Very Good'),
            ('Gd', 'Good')
        ]
    media_condition = forms.ChoiceField(choices=grading_choices)
    sleeve_condition = forms.ChoiceField(choices=grading_choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        genres = Genre.objects.all().order_by('name')
        genre_friendly_names = [(c.id, c.get_friendly_name()) for c in genres]
        artists = Artist.objects.all().order_by('name')
        artist_friendly_names = [(c.id, c.get_friendly_name()) for c in
                                 artists]

        record_labels = Recordlabel.objects.all().order_by('name')
        record_label_friendly_names = [(c.id, c.get_friendly_name()) for c in
                                       record_labels]

        self.fields['genre'].choices = genre_friendly_names
        self.fields['artist'].choices = artist_friendly_names
        self.fields['record_label'].choices = record_label_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Name',
            'friendly_name': 'Friendly Name',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = placeholders[field]

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class RecordLabelForm(forms.ModelForm):

    class Meta:
        model = Recordlabel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Name',
            'friendly_name': 'Friendly Name',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = placeholders[field]

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'product', 'created_on')

    review_rating = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'review_rating': 'Review Rating',
            'review_title': 'Review Title',
            'review_content': 'Review Content',
        }

        self.fields['review_rating'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = placeholders[field]

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

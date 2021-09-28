from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Full Name',
            'contact_email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = placeholders[field]

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

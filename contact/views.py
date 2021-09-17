from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    """ Manage the contact form page """

    form = ContactForm(request.POST or None)
    context = {
        'form': form,
    }
    template = 'contact/contact.html'
    return render(request, template, context)

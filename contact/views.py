from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """ Manage the contact form page """

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            """Send the user a confirmation email"""

            email = contact_form.cleaned_data['contact_email']
            full_name = contact_form.cleaned_data['name']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            print(email)
            subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt')
            body = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {
                    'full_name': full_name,
                    'subject': subject,
                    'message': message,
                    'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [email]
            )

            messages.success(request, 'Your message was submitted successfully.' \
                ' We will be in touch soon')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'There was a problem with the form. Please resubmit')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    template = 'contact/contact.html'
    return render(request, template, context)

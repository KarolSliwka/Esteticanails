from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from .forms import ContactForm
from .models import ContactHeader


def contact(request):
    """ A view to render Contact Page including Contact Form """

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            from_email = contact_form.cleaned_data['from_email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

            html_msg = render_to_string(
                'includes/emails/email.html', {'name': name, 'subject': subject,
                                               'message': message, 'from_email': from_email})
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                          html_message=html_msg, fail_silently=False)

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('/contact', messages.success(request,
                                                         'Dear ' + name.title() + ', thanks for your message!  \
                                        I will replay as soon as I get there'))
        else:
            return redirect('/contact',
                            messages.info(request, 'Something went wrong..'))

    else:
        contact_form = ContactForm()

    if ContactHeader.objects.count() != 0:
        contact_info = ContactHeader.objects.first()
        context = {
            'contact_form': contact_form,
            'contact_info': contact_info,
        }
    else:
        context = {
            'contact_form': contact_form,
        }

    template = 'contact/contact.html'

    return render(request, template, context)

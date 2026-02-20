from ipaddress import ip_address

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from lawyer_website import settings


def get_client_ip(request):
    """
    Get user's IP
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    return ip


def send_contact_email_message(name, phone, message):
    """
    Function to send feedback form data to email
    """
    message = render_to_string('lawyer/feedback_email_send.html', {
        'name': name,
        'phone': phone,
        'message': message,
    })
    email = EmailMessage(f'{name} tel.:{phone}', message, settings.SERVER_EMAIL, [settings.EMAIL_ADMIN,])
    email.send(fail_silently=False)

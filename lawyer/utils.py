from ipaddress import ip_address


from django.contrib.auth.models import User
import requests

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from lawyer_website import settings
from lawyer_website.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


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


def send_telegram_message(text, parse_mode='HTML'):
    """
    Отправляет сообщение в Telegram
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text,
        'parse_mode': parse_mode
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка отправки в Telegram: {e}")
        print(f"Ответ: {response.text}")
        return None
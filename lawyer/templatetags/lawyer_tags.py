from django import template

from lawyer.models import Advantage, Service, ServiceCategory, Contact

#--------------------------------------------------

register = template.Library()

menu = []
for c in ServiceCategory.objects.all():
    menu.append({'title': c.name, 'url_name': f"#{c.anchor}"})
menu.append({'title': "Оставить сообщение", 'url_name': '#request'})

contacts = []
for c in Contact.objects.all():
    contacts.append({'href': c.href, 'pic': c.pic, 'alt': c.alt, 'text': c.text})

# menu2 = [
#     # {'title': "Главная", 'url_name': 'lawyer:home'},
#     # {'title': "Оставить сообщение", 'url_name': 'lawyer:feedback'},
#     {'title': "Частным лицам", 'url_name': '#service-private'},
#     {'title': "Бизнесу", 'url_name': '#service-business'},
#     {'title': "Оставить сообщение", 'url_name': '#request'},
# ]

# contacts = [
#     {'href': "tel:+79495372567", 'src': "lawyer/img/phone_01.png", 'alt': "Телефон", 'text': "+7(949)537-25-67"},
#     {'href': "https://t.me/+79495372567", 'src': "lawyer/img/tg_01.png", 'alt': "Telegram", 'text': "Telegram"},
#     {'href': "https://vk.com/id78401004", 'src': "lawyer/img/vk_01.png", 'alt': "ВКонтакте", 'text': "ВКонтакте"},
#     {'href': "mailto:volodiashapiro@yandex.ru", 'src': "lawyer/img/email_01.png", 'alt': "E-Mail", 'text': "volodiashapiro@yandex.ru"},
#     {'href': "#message", 'src': "lawyer/img/message_01.png", 'alt': "Сообщение", 'text': "Оставить сообщение"},
# ]


@register.simple_tag
def get_menu():
    return menu


@register.simple_tag
def get_contacts():
    return contacts


@register.simple_tag
def get_advantages():
    advantages = Advantage.objects.all()
    return advantages


@register.simple_tag
def get_services():
    services = Service.objects.all()
    return services

@register.simple_tag
def get_service_categories():
    service_categories = ServiceCategory.objects.all()
    return service_categories

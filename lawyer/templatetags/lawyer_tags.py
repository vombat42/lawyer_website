from django import template


#--------------------------------------------------

register = template.Library()

menu = [
    # {'title': "Главная", 'url_name': 'lawyer:home'},
    # {'title': "Оставить сообщение", 'url_name': 'lawyer:feedback'},
    {'title': "Частным лицам", 'url_name': '#service-private'},
    {'title': "Бизнесу", 'url_name': '#service-business'},
    {'title': "Оставить сообщение", 'url_name': '#request'},
]

contacts = [
    {'href': "tel:+79495372567", 'src': "lawyer/img/phone_01.png", 'alt': "Телефон", 'text': "+7(949)537-25-67"},
    {'href': "https://t.me/+79495372567", 'src': "lawyer/img/tg_01.png", 'alt': "Telegram", 'text': "Telegram"},
    {'href': "https://vk.com/id78401004", 'src': "lawyer/img/vk_01.png", 'alt': "ВКонтакте", 'text': "ВКонтакте"},
    {'href': "mailto:volodiashapiro@yandex.ru", 'src': "lawyer/img/email_01.png", 'alt': "E-Mail", 'text': "volodiashapiro@yandex.ru"},
    {'href': "#message", 'src': "lawyer/img/message_01.png", 'alt': "Сообщение", 'text': "Оставить сообщение"},
]


# menu_local = [
#     {'title': "Частным лицам", 'url_name': '#service-private'},
#     {'title': "Бизнесу", 'url_name': '#service-business'},
#     {'title': "Оставить сообщение", 'url_name': '#request'},
# ]

@register.simple_tag
def get_menu():
    return menu


@register.simple_tag
def get_contacts():
    return contacts
my_django_secret_key = '*******************'


my_allowed_hosts = ['192.168.0.1', '127.0.0.1']

# my_debug = False
my_debug = True

my_pg_connect = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "",
    "USER": "",
    "PASSWORD": "",
    "HOST": "127.0.0.1",
    "PORT": "5432",
}

my_drf_rendered_classes = [
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
]

my_email_host_user = ""
my_email_host_password = ""
my_email_host = "smtp.****.**"
my_email_host_port = 465
my_email_use_ssl = False
my_email_use_tls = True

my_email_admin = "*****@****.**"

my_site = 'lawyer_website'

my_csrf_trusted_origins = ['https://192.168.0.1', '127.0.0.1']
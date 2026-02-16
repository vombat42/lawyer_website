from django.core.validators import FileExtensionValidator
from django.db import models

# ----------------------------------------------------------------
class Advantage(models.Model):
	"""
	мои преимущества
	"""
	text = models.TextField(max_length=255, blank=False, verbose_name='Преимущество')

	def __str__(self):
		return self.text[:10]

	class Meta:
		verbose_name = "Преимущество"
		verbose_name_plural = "Преимущества"
		# ordering = ['']


class Contact(models.Model):
    """
    контакты
    """
    href = models.CharField(max_length=50, blank=False, verbose_name='href')
    alt = models.CharField(max_length=50, blank=False, verbose_name='alt')
    text = models.CharField(max_length=50, blank=False, verbose_name='text')
    order = models.IntegerField(verbose_name='Порядок расположения')
    pic = models.ImageField(
        verbose_name='Изображение',
        upload_to='img/',
        default='img/contact_default.png',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ['order']


class ServiceCategory(models.Model):
    """
    категории услуг
    """
    name = models.CharField(max_length=20, verbose_name='Категория услуг')
    description = models.TextField(max_length=40,blank=True, verbose_name='Описание')
    order = models.IntegerField(verbose_name='Порядок расположения')
    anchor = models.CharField(max_length=20, verbose_name='id-якорь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория услуг"
        verbose_name_plural = "Категории услуг"
        ordering = ['order',]


class Service(models.Model):
    """
    Услуги
    """
    text = models.TextField(max_length=255, blank=False, verbose_name='Услуга')
    category = models.ForeignKey('ServiceCategory', on_delete=models.PROTECT, verbose_name='Категория услуг')
    pic = models.ImageField(
        verbose_name='Изображение',
        upload_to='img/',
        default='img/service_default.png',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['category', ]


class Feedback(models.Model):
    """
    Модель обратной связи
    """
    subject = models.CharField(max_length=255, verbose_name='Тема письма')
    email = models.EmailField(max_length=255, verbose_name='Электронная почта (email)')
    content = models.TextField(verbose_name='Содержимое письма')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    ip_address = models.GenericIPAddressField(verbose_name='IP отправителя',  blank=True, null=True)
    # user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']
        db_table = 'app_feedback'

    def __str__(self):
        return f'Вам письмо от {self.email}'

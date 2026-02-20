from django.contrib import admin

from django.contrib import admin

from lawyer.models import Advantage, Feedback, ServiceCategory, Service, Contact


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    """
    Админ-панель модели преимуществ
    """
    list_display = ('text',)
    list_display_links = ('text',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Админ-панель модели контактов
    """
    list_display = ('order', 'href', 'alt', 'text', 'pic', )
    list_display_links = ('order', 'href', 'alt', 'text', 'pic', )


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    """
    Админ-панель модели категорий услуг
    """
    list_display = ('name', 'description', 'order', 'anchor', )
    list_display_links = ('name', 'description', 'order', 'anchor', )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Админ-панель модели услуг
    """
    list_display = ('text', 'category', 'pic', )
    list_display_links = ('text', 'category', )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админ-панель модели обратной связи
    """
    list_display = ('name', 'phone', 'time_create', 'ip_address')
    list_display_links = ('name', 'phone', 'time_create', 'ip_address')
    readonly_fields = ('time_create', )

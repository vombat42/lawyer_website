from django.shortcuts import render
from .models import Setting

class SettingModeMiddleware:
    """
    отображает "заглушку" вместо сайта, если включена такая настройка
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Проверяем, включен ли режим обслуживания
        try:
            setting_503 = Setting.objects.filter(name='503').first()
            if setting_503 and setting_503.is_active:
                # Показываем страницу заглушки
                if not request.path.startswith('/admin/'):
                    return render(request, 'lawyer/503.html', status=503)
        except Setting.DoesNotExist:
            pass # Если записи нет, игнорируем

        response = self.get_response(request)
        return response
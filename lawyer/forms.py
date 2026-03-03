import re

from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from lawyer.models import Feedback

# CAPTCHA
class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'lawyer/custom_captcha.html'


class FeedbackForm(forms.ModelForm):
    """
    Форма отправки обратной связи
    """
    captcha = CaptchaField( widget=CustomCaptchaTextInput,
                            error_messages = {
                                'invalid': 'Неверно введена капча! Попробуйте ещё раз.',
                                'required': 'Пожалуйста, введите капчу'
                            },
                            label='Введите код с картинки')

    # Новое поле для ввода (без привязки к модели)
    phone_input = forms.CharField(
        max_length=18,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'telephone',
            'id': 'form-phone',
            'type': 'tel',
            'placeholder': "+7 (___) ___-___-___ *"}),
    )

    class Meta:
        model = Feedback
        # fields = ('name', 'phone', 'message',)
        exclude = ['phone']  # Исключаем phone из формы полностью!
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name', 'id': 'form-name', 'placeholder': "Ваше имя *"}),
            'phone': forms.HiddenInput(),  # скрываем поле модели
            'message': forms.Textarea(attrs={'class': 'message', 'id': 'form-message', 'placeholder': "Ваше сообщение *"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_phone_input(self):
        phone_input = self.cleaned_data.get('phone_input')

        if not phone_input:
            raise forms.ValidationError('Введите номер телефона')

        # Очищаем до цифр
        import re
        digits = re.sub(r'\D', '', phone_input)

        # Обрезаем до 11 цифр
        if len(digits) > 11:
            digits = digits[:11]

        # Проверяем длину
        if len(digits) != 11:
            raise forms.ValidationError('Номер должен содержать 11 цифр')

        # Сохраняем очищенные цифры для использования в save
        self.cleaned_data['phone_clean'] = digits

        return phone_input  # возвращаем как есть для отображения


    def save(self, commit=True):
        instance = super().save(commit=False)

        # Устанавливаем phone из очищенного поля phone_input
        if 'phone_input' in self.cleaned_data:
            instance.phone = self.cleaned_data['phone_input']

        if commit:
            instance.save()

        return instance


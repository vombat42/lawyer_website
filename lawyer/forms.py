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
        # self.fields['phone'].required = False
        # Принудительно добавляем поле, если его нет
        print('INIT------------')
        if 'phone_input' not in self.fields:
            print('TTTT-----UUUUU')
        # для символов оформления номера телефона (скобки, дефисы, пробелы)
        # Если редактируем существующий объект, показываем его номер в phone_input
        # if self.instance and self.instance.phone:
        #     p = self.instance.phone
        #     if len(p) == 11:
        #         self.initial['phone_input'] = f"+7 ({p[1:4]}) {p[4:7]}-{p[7:9]}-{p[9:11]}"


    def clean_phone_input(self):
        phone_input = self.cleaned_data.get('phone_input')
        print(f"++++++++++++++++++clean_phone_input: {phone_input}")  # отладка

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
            print(f"Устанавливаем phone: {instance.phone}")  # отладка


        if commit:
            instance.save()
            print(f"Объект сохранён с phone: {instance.phone}")  # отладка

        return instance





    #
    # def clean_phone(self):
    #     print('*0*****************************')
    #     phone = self.cleaned_data.get('phone')
    #     digits_only = ''
    #     print('*1*****************************', phone)
    #     if phone:
    #         # Удаляем всё, кроме цифр и обрезаем до 11
    #         digits_only = re.sub(r'\D', '', phone)[:11]
    #         print('*2*****************************', digits_only)
    #         if len(digits_only) < 11:
    #             print('*3*****************************', digits_only)
    #             raise forms.ValidationError('Номер должен содержать 11 цифр')
    #
    #     print('*4*****************************', digits_only)
    #
    #     return digits_only
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

    # captcha = CaptchaField()
    captcha = CaptchaField( widget=CustomCaptchaTextInput,
                            error_messages = {
                                'invalid': 'Неверно введена капча! Попробуйте ещё раз.',
                                'required': 'Пожалуйста, введите капчу'
                            },
                            label='Введите код с картинки')

    # captcha = CaptchaField( error_messages = {
    #                             'invalid': 'Неверно введена капча! Попробуйте ещё раз.',
    #                             'required': 'Пожалуйста, введите капчу'
    #                         },
    #                         label='Введите код с картинки')
    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'message',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name', 'id': 'form-name', 'placeholder': "Ваше имя *"}),
            'phone': forms.TextInput(attrs={'class': 'telephone', 'id': 'form-phone', 'placeholder': "+7 (___) ___-___-___ *"}),
            'message': forms.Textarea(attrs={'class': 'message', 'id': 'form-message', 'placeholder': "Ваше сообщение *"}),
        }

    # def __init__(self, *args, **kwargs):
    #     """
    #     Обновление стилей формы
    #     """
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})
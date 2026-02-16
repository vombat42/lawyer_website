from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from lawyer.models import Feedback

# CAPTCHA
class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'lawyer/custom_captcha.html'


class FeedbackCreateForm(forms.ModelForm):
    """
    Форма отправки обратной связи
    """

    # captcha = CaptchaField()
    captcha = CaptchaField(widget=CustomCaptchaTextInput, label='Введите код с картинки')

    class Meta:
        model = Feedback
        fields = ('subject', 'email', 'content')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})
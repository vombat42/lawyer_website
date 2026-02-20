from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView

from .models import Feedback
from .forms import FeedbackForm
from .utils import get_client_ip, send_contact_email_message, send_telegram_message


#----------------------------------------------------------------------------

def index(request):
    form = FeedbackForm()
    return render(request, 'lawyer/home.html', context={'title': 'Юрист - Главная',})


class LawyerHome(FormView):
    # form = FeedbackForm
    form_class = FeedbackForm
    template_name = 'lawyer/home.html'
    extra_context = {'title': 'Ваш Юрист',}
    # messages.add_message(request, messages.INFO, "Hello world.")
    success_url = reverse_lazy('lawyer:home')  # URL для редиректа после успеха

    def form_valid(self, form):
        # Отправляем сообщение
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            # send_contact_email_message(feedback.name, feedback.phone, feedback.message)
            send_telegram_message(f'Имя: {feedback.name}\nТелефон: {feedback.phone}\nСообщение: {feedback.message}')
            # Сохраняем данные
            feedback.save()
            messages.success(self.request, 'Ваше сообщение отправлено.')

        return super().form_valid(form)

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


from .models import Feedback
from .forms import FeedbackCreateForm
from .utils import get_client_ip, send_contact_email_message


#----------------------------------------------------------------------------

def index(request):
    return render(request, 'lawyer/home.html', context={'title': 'Юрист - Главная',})

class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    success_message = 'Ваше письмо успешно отправлено администрации сайта'
    template_name = 'lawyer/feedback.html'
    extra_context = {'title': 'Контактная форма'}
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            send_contact_email_message(feedback.subject, feedback.email, feedback.content, feedback.ip_address)
        return super().form_valid(form)
from django.urls import path, include

from .views import index, FeedbackCreateView

app_name = 'lawyer'


urlpatterns = [
    path('', index, name='home'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]
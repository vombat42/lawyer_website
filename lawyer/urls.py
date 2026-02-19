from django.urls import path, include

from .views import index, LawyerHome

app_name = 'lawyer'


urlpatterns = [
    # path('', index, name='home'),
    path('', LawyerHome.as_view(), name='home'),
    # path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]
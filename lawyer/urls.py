from django.urls import path, include

from .views import index, LawyerHome
from lawyer_website import secret

app_name = 'lawyer'

# zaglushka = 1

if secret.zaglushka == 0:
    urlpatterns = [
        # path('', index, name='zaglushka'),
        path('', LawyerHome.as_view(), name='home'),
        # path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
    ]
else:
    urlpatterns = [
        path('', index, name='zaglushka'),
        # path('', LawyerHome.as_view(), name='home'),
        # path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
    ]

# urlpatterns = [
#     # path('', index, name='zaglushka'),
#     path('', LawyerHome.as_view(), name='home'),
#     # path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
# ]
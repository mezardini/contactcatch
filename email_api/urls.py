from django.urls import path
from .views import SendEmail
urlpatterns = [
    path('sendemail/', SendEmail.as_view(), name='SE')
]

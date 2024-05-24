from django.urls import path
from .views import SendEmail, SendEmailFF
urlpatterns = [
    path('sendemail/', SendEmail.as_view(), name='SE'),
    path('sendemailFF/', SendEmailFF.as_view(), name='SEFF')
]

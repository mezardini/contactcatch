from django.shortcuts import render
from .serializers import MessageSerializer
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework import generics, status, viewsets
# Create your views here.


class SendEmailApi(generics.CreateAPIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            sender_email = serializer.validated_data.get('sender_email')
            subject = serializer.validated_data.get('subject')
            body = serializer.validated_data.get('body')
            recipient_email = serializer.validated_data.get('recipient_email')

            send_mail(
            subject + ' from ' + sender_email,
            body,
            'settings.EMAIL_HOST_USER',
            [recipient_email],
            fail_silently=False,
        )
            

class SendEmailApp(generics.CreateAPIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            sender_email = serializer.validated_data.get('sender_email')
            subject = serializer.validated_data.get('subject')
            body = serializer.validated_data.get('body')
            recipient_email = serializer.validated_data.get('recipient_email')

            send_mail(
            subject + ' from ' + sender_email,
            body,
            'settings.EMAIL_HOST_USER',
            [recipient_email],
            fail_silently=False,
        )
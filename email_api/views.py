from django.shortcuts import render, redirect
# from .serializers import MessageSerializer
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import generics, status, viewsets
# Create your views here.


# class SendEmailApi(generics.CreateAPIView):
#     def post(self, request):
#         serializer = MessageSerializer(data=request.data)
#         if serializer.is_valid():
#             sender_email = serializer.validated_data.get('sender_email')
#             subject = serializer.validated_data.get('subject')
#             body = serializer.validated_data.get('body')
#             recipient_email = serializer.validated_data.get('recipient_email')

#             send_mail(
#             subject + ' from ' + sender_email,
#             body,
#             'settings.EMAIL_HOST_USER',
#             [recipient_email],
#             fail_silently=False,
#         )


# class SendEmailApp(generics.CreateAPIView):
#     def post(self, request):
#         serializer = MessageSerializer(data=request.data)
#         if serializer.is_valid():
#             sender_email = serializer.validated_data.get('sender_email')
#             subject = serializer.validated_data.get('subject')
#             body = serializer.validated_data.get('body')
#             recipient_email = serializer.validated_data.get('recipient_email')

#             send_mail(
#             subject + ' from ' + sender_email,
#             body,
#             'settings.EMAIL_HOST_USER',
#             [recipient_email],
#             fail_silently=False,
#         )


class SendEmail(generics.CreateAPIView):
    def post(self, request):
        # serializer = MessageSerializer(data=request.data)
        # if serializer.is_valid():
        email = request.data.get('email')
        name = request.data.get('name')
        project_name = request.data.get('project_name')
        project_url = request.data.get('project_url')
        message = request.data.get('message')

        send_mail(
            name + ' from ' + email,
            message + project_name + project_url,
            'settings.EMAIL_HOST_USER',
            ['mezardini@gmail.com'],
            fail_silently=False,
        )
        return redirect('https://feedbackflow.netlify.app/')

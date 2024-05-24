from django.shortcuts import render, redirect
from .serializers import SendEmailSerializer
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
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

        subject = f'Message from {name} with email of: {email}'
        body = f"Hello Mezard,\n\nYou have received a project review request for {project_name}.\nProject URL: {project_url}\n\nMessage: {message}\n"

        send_mail(
            subject,
            body,
            'settings.EMAIL_HOST_USER',
            ['mezardini@gmail.com'],
            fail_silently=False,
        )
        return redirect('https://feedbackflow.netlify.app/')


class SendEmailFF(generics.CreateAPIView):
    serializer_class = SendEmailSerializer

    def post(self, request):

        # redirect_url = 'https://feedbackflow.netlify.app/'
        email = request.data.get('email')
        name = request.data.get('name')
        message = request.data.get('message')
        recipient = request.data.get('recipient')
        redirect_url = request.data.get('redirect_url')

        subject = f'Message from {name}'
        body = f'''
        Hello Mezard,\n
        You have received a message from {name}.\n
        With email: {email}\n
        Message: {message}\n'''

        send_mail(
            subject,
            body,
            'settings.EMAIL_HOST_USER',
            [recipient],
            fail_silently=False,
        )
        # print(redirect_url)
        return redirect(redirect_url)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

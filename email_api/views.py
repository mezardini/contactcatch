from django.shortcuts import render, redirect
from .serializers import SendEmailSerializer
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from django.core.mail import EmailMessage

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


html_template = '''
<body style="background-color: #f7f5fa; margin: 0 !important; padding: 0 !important;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
            <td bgcolor="#426899" align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="480">
                    <tr>
                        <td align="center" valign="top" style="padding: 40px 10px 40px 10px;">
                            <div style="display: block; font-family: Helvetica, Arial, sans-serif; color: #ffffff; font-size: 18px;"
                                border="0"></div>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#426899" align="center" style="padding: 0px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="480">
                    <tr>
                        <td bgcolor="#ffffff" align="left" valign="top"
                            style="padding: 30px 30px 20px 30px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; line-height: 48px;">
                            <!-- Add your header content here -->
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="480">
                    <tr>
                        <td bgcolor="#ffffff" align="left">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <th align="left" valign="top"
                                        style="padding-left:30px;padding-right:15px;padding-bottom:10px; font-family: Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                                        E-Mail</th>
                                    <td align="left" valign="top"
                                        style="padding-left:15px;padding-right:30px;padding-bottom:10px;font-family: Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                                        {email}</td>
                                </tr>
                                <tr>
                                    <th align="left" valign="top"
                                        style="padding-left:30px;padding-right:15px;padding-bottom:10px; font-family: Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                                        Name</th>
                                    <td align="left" valign="top"
                                        style="padding-left:15px;padding-right:30px;padding-bottom:10px;font-family: Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                                        {name}</td>
                                </tr>
                                <tr>
                                    <td colspan="2"
                                        style="padding-left:30px;padding-right:15px;padding-bottom:10px; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 25px;">
                                        <p>Message:</p>
                                        <p>{message}</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
'''


def generate_email_html(email, name, message):
    return html_template.format(email=email, name=name, message=message)


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
        # body = f'''
        # Hello Mezard,\n
        # You have received a message from {name}.\n
        # With email: {email}\n
        # Message: {message}\n'''
        body = generate_email_html(email, name, message)

        # send_mail(
        #     subject,
        #     body,
        #     'settings.EMAIL_HOST_USER',
        #     [recipient],
        #     fail_silently=False,
        # )
        email_message = EmailMessage(
            subject,
            body,
            'settings.EMAIL_HOST_USER',
            [recipient]
        )
        email_message.content_subtype = "html"  # Set the content type to HTML

        email_message.send(fail_silently=False)
        # print(redirect_url)
        return redirect(redirect_url)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

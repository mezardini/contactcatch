from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.core.validators import RegexValidator


class MessageSerializer(serializers.FormSerializer):
    sender_email = serializers.EmailField(validators=[
        RegexValidator(
            regex=r'^[\w\.-]+@[\w\.-]+\.\w+$',
            message='Enter a valid email address.',
            code='invalid_email'
        )
    ])
    recipient_email = serializers.EmailField(validators=[
        RegexValidator(
            regex=r'^[\w\.-]+@[\w\.-]+\.\w+$',
            message='Enter a valid email address.',
            code='invalid_email'
        )
    ])
    subject = serializers.CharField()
    body = serializers.CharField()
from rest_framework import serializers


class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=1000)
    recipient = serializers.EmailField()

    def validate(self, data):
        """
        Check that the message is not empty.
        """
        if not data.get('message').strip():
            raise serializers.ValidationError("Message cannot be empty.")
        return data

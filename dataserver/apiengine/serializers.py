from .models import MessageModel
from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MessageModel
        fields = ('date', 'time','vinput', 'voutunfiltered', 'runfiltered', 'voutfiltered', 'rfiltered', 'frequency' )

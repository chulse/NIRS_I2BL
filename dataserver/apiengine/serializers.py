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
        fields = ( 'date', 'pd1r1', 'pd2r1', 'pd3r1', 'pd1ir1', 'pd2ir1', 'pd3ir1', 'pd1r2', 'pd2r2', 'pd3r2', 'pd1ir2', 'pd2ir2', 'pd3ir2', 'pd1r3', 'pd2r3', 'pd3r3', 'pd1ir3', 'pd2ir3', 'pd3ir3','processedData')

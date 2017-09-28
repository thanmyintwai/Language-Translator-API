from rest_framework import serializers

class TranslatorSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    dest = serializers.CharField(required=False)
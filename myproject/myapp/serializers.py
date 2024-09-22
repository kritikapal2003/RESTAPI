# myapp/serializers.py

from rest_framework import serializers

class RequestDataSerializer(serializers.Serializer):
    data = serializers.ListField(
        child=serializers.CharField()
    )
    file_b64 = serializers.CharField(required=False, allow_blank=True)

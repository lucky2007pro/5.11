from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    name = serializers.CharField()
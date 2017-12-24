from rest_framework import serializers

class CabifySerializer(serializers.Serializer):
    ''' Serializes a name field to test our apiview '''

    name = serializers.CharField(max_length=10)
    surname = serializers.CharField(max_length=10)
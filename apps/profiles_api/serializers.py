from rest_framework import serializers
from . import models

class CabifySerializer(serializers.Serializer):
    ''' Serializes a name field to test our apiview '''

    name = serializers.CharField(max_length=10)
    surname = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer for our user profile objects
    """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return a new user """

        user = models.UserProfile(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ A serializer for profile feed items """
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user', 'status_text', 'date')
        extra_kwargs = {'user': {'read_only': True}}
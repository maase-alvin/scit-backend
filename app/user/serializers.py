"""
Serializers for user API Views
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the users object
    """
    class Meta:
        """
        Meta class for the users object
        """
        model = get_user_model()
        fields = ('email', 'password', 'name', 'profile')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """
        Create a new user with encrypted password and return it
        """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """
        Update a user, setting the password correctly and return it
        """
        password = validated_data.pop('password', None)
        # pop() removes the password from the dictionary
        # and returns the value of the password
        user = super().update(instance, validated_data)
        # super() returns a proxy object that delegates method calls
        # to a parent or sibling class of type.
        # https://docs.python.org/3/library/functions.html#super
        if password:
            user.set_password(password)
            user.save()
        return user

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')
        
        attrs['user'] = user
        return attrs
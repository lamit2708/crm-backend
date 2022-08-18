from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

# from rest_framework.response import Response
# from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
# https://www.codersarts.com/post/how-to-create-register-and-login-api-using-django-rest-framework-and-token-authentication
# Login
# https://studygyaan.com/django/django-rest-framework-tutorial-register-login-logout


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        # token['fav_color'] = user.fav_color
        #token['username'] = user.username
        #token['groups'] = user.groups.values_list('name', flat=True)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['id'] = self.user.id
        data['username'] = self.user.username
        #data['fullname'] = self.user.fullname
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['email'] = self.user.email
        data['groups'] = self.user.groups.values_list('name', flat=True)
        return data


class UserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    # email = serializers.EmailField(
    #     required=True
    # )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        #fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'is_staff', 'is_active', 'last_login', 'date_joined')
        fields = ('id', 'username',  'password',
                  'email', 'first_name', 'last_name')  # first_name, #last_name
        # extra_kwargs = {'password': {'write_only': True},
        #                 'last_login': {'read_only': True},
        #                 'date_joined': {'read_only': True}}

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance


# Serializer to Register User
# UserSerializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    #password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        #fields = ('username', 'password', 'password2','email', 'first_name', 'last_name')
        #fields = ('username', 'password', 'password2', 'email')
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True},
                        'first_name': {'required': True},
                        'last_name': {'required': True}}
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."})
    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        #password = validated_data.pop('password', None)
        user.is_active = True

        user.set_password(validated_data['password'])
        # user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.save()
        return user

    # def create_user(self, email, username, password, alias=None):
    #     user = self.model(
    #         email=self.normalize_email(email),
    #         username=username,)
    #     user.set_password(make_password(password))
    #     user.save()
    #     return user

    # def create_superuser(self, email, username, password):
    #     self.create_user(email, username, password)
    #     user.is_staff()
    #     user.is_superuser = True
    #     user.save()
    #     return user

# Custom Serializer for custom jwt

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

# Check access token
# https://jwt.io/#debugger-io


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Override get_token of TokenObtainPairSerializer
    def get_token(cls, user):
        # Get token from TokenObtainPairSerializer
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        # Adding role to token
        token['group_id'] = user.groups.all()[0].id
        token['group_name'] = user.groups.all()[0].name

        return token

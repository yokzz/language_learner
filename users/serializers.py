from rest_framework import routers, serializers, viewsets
from django.contrib.auth import get_user_model  
from users.models import Profile
from django.db import transaction

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['picture', 'name', 'surname', 'phone']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic 
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
        user.save() 
        return user
    

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password1', 'password2']
        
    
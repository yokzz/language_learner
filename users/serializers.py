from rest_framework import routers, serializers, viewsets
from django.contrib.auth import get_user_model  

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'username', 'password']

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.password = validated_data.get('password')
        return instance
    
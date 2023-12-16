from .models import Usuarios
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
    
    
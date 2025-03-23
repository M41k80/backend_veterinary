from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # La contraseña no se devuelve en las respuestas

    class Meta:
        model = User
        fields = ['username', 'password', 'role']

    def create(self, validated_data):
        # Extrae la contraseña del diccionario validated_data
        password = validated_data.pop('password')
        
        # Crea el usuario
        user = User(**validated_data)
        user.set_password(password)  # Hashea la contraseña
        user.save()  # Guarda el usuario en la base de datos
        
        return user
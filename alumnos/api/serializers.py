from rest_framework import serializers
from alumnos.models import Alumno
from django.contrib.auth.models import User

class AlumnosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('nombre','primer_apellido','segundo_apellido')

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validate_data):
            password = validate_data['password']
            password2 = validate_data['password2']
            if password != password2:
                raise serializers.ValidationError({"Error":"Las contraseñas no coinciden "})

            if User.objects.filter(email=validate_data['email']).exists():
                raise serializers.ValidationError({'Error': 'El email del usuario ya existe'})

            if User.objects.filter(username=validate_data['username']).exists():
                raise serializers.ValidationError({'Error': 'El usuario ya existe'})

            user = User(email=validate_data['email'], username=validate_data['username'])
            user.set_password(password)
            user.save()
            return user
from alumnos.api.serializers import RegistrationSerializer, AlumnosSerializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def Registration_view(request):
    if request.method == "POST":
        user_serializar = RegistrationSerializer(data=request.data)

        if user_serializar.is_valid():
            user = user_serializar.save()

            token = Token.objects.get(user=user).key

            data = {}

            alumno_data = {
                'user': user.id,
                'nombre': user.data.get('nombre'),
                'primer_apellido': user.data.get('primer_apellido'),
                'segundo_apellido': user.data.get('segundo_apellido'),
                'sexo': user.data.get('sexo'),
                'fecha_nacimiento': user.data.get('fecha_nacimiento'),
                'edad': user.data.get('edad'),
                'curp': user.data.get('curp'),
                'descripcion':user.data.get('descripcion'),
                'imagen': user.data.get('imagen'),
                'clases' : user.data.get('clases')
            }

            alumno_serializer = AlumnosSerializers(data=alumno_data)

            if alumno_serializer.is_valid():
                alumno_serializer.save()

                data['username'] = user.username
                data['token'] = token

                return Response(data, status=status.HTTP_201_CREATED)

            else:
                user.delete()
                return Response(alumno_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(user_serializar.errors, status=status.HTTP_400_BAD_REQUEST)
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

def custom_upload_to(instance, filename):
    return f'alumnos/{filename}'

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='alumno')
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField(max_length=15)
    edad = models.IntegerField()
    curp = models.CharField(max_length=18, unique=True)
    descripcion = models.CharField(max_length=400)
    imagen = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    clases = models.ManyToManyField('clases.Clase', related_name='alumnos_rel', blank=True)

    def __str__(self):
        return f'''
        Nombre: {self.nombre} {self.primer_apellido} {self.segundo_apellido}
        Descripcion: {self.descripcion}
        Imagen: {self.imagen}
        '''

@receiver(pre_save, sender=Alumno)
def asignar_avatar(sender, instance, **kwargs):
    if instance.sexo == 'H':
        instance.imagen = 'man.png'
    elif instance.sexo == 'M':
        instance.imagen = 'woman.png'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

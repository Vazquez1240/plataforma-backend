from django.db import models

# Create your models here.

class Clase(models.Model):
    titulo_clase = models.CharField(max_length=50)
    alumnos = models.ManyToManyField('alumnos.Alumno', related_name='clases_rel', blank=True, default=None)
    profesor = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo_clase
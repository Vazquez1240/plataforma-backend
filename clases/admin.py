from django.contrib import admin
from alumnos.models import Alumno
from clases.models import Clase
# Register your models here.

admin.site.register(Clase)
admin.site.register(Alumno)
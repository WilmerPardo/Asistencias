from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

class RegistroAsistencia(models.Model):
    fecha = models.DateField()


class Materia(models.Model):
    nombre  = models.CharField(max_length=50)

class Estudiante(Persona):
    paralelo = models.CharField(max_length=1)
    #estudianteList = models.ForeignKey(RegistroAsistencia, on_delete=models.CASCADE)
    materiaList = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="estudianteList")


class RegistroAsistencia(models.Model):
        fecha = models.DateField()


class Profesor(Persona):
    materiaList = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="profesorList")
    registroAsistencia = models.ForeignKey(RegistroAsistencia, on_delete=models.CASCADE)
    def __str__(self):
        return self.persona




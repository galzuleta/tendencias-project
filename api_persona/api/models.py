from django.db import models

class Docentes (models.Model):
    titulo=models.CharField(max_length=80)

class Estudiantes (models.Model):
    matricula=models.CharField(max_length=80) 

class Persona (models.Model):
    cedula= models.IntegerField()
    nombres= models.CharField(max_length=80)
    apellidos= models.CharField(max_length=80)
    fecha_creacion = models.DateField(auto_now=True)
    nacionalidad = models.CharField(max_length=80)
    titulo = models.ForeignKey(Docentes, on_delete=models.PROTECT)
    matricula = models.ForeignKey(Estudiantes, on_delete=models.PROTECT)
    email =  models.CharField(max_length=80)
    phone =  models.CharField(max_length=80)
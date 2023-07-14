# Create your models here.
from django.db import models


class Persona(models.Model):
    OPCIONES_CARGO = (
        ('decano', 'Decano'),
        ('docente', 'Docente'),
        ('estudiante', 'Estudiante'),
        ('director', 'Director'),
    )

    cedula = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cargo = models.CharField(max_length=20, choices=OPCIONES_CARGO)

    def info_docente(self):
        return "|{}|{}|  {} {}".format(self.cedula, self.cargo, self.nombres, self.apellidos)

    def __str__(self):
        return self.info_docente()

class Carrera(models.Model):
    nombre = models.CharField(max_length=60)
    facultad = models.CharField(max_length=200)
    inicio_periodo = models.DateField()
    final_periodo = models.DateField()

    def info_carrera(self):
        return "|{}|{}| periodo: {} hasta {}".format(self.nombre, self.facultad, self.inicio_periodo, self.final_periodo)
    def __str__(self):
        return self.info_carrera()

class Asignatura(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, default=0)
    nombre = models.CharField(max_length=60)
    ciclo = models.CharField(max_length=20)
    paralelo = models.CharField(max_length=5)

    def info_asignatura(self):
        return "{} - {} - {} - {}".format(self.carrera, self.nombre, self.ciclo, self.paralelo)

    def __str__(self):
        return self.info_asignatura()

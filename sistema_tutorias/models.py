# Create your models here.
from django.db import models


class Persona(models.Model):
    OPCIONES_CARGO = (
        ('decano', 'Decano'),
        ('docente', 'Docente'),
        ('estudiante', 'Estudiante'),
        ('director', 'Director'),
    )
    cargo = models.CharField(max_length=20, choices=OPCIONES_CARGO)
    cedula = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    def info_docente(self):
        return "|{}|{}|  {} {}".format(self.cargo, self.cedula, self.nombres, self.apellidos)

    def __str__(self):
        return self.info_docente()

class Carrera(models.Model):
    OPCIONES_FACULTAD = (
        ('agropecuaria', 'Agropecuaria y de Recursos Naturales Renovables'),
        ('educación', 'Educación, el Arte y la Comunicación'),
        ('energía', 'Energía, las Industrias y los Recursos Naturales no Renovables'),
        ('jurídica', 'Jurídica, Social y Administrativa'),
        ('salud', 'Salud Humana'),
        ('distancia', 'Unidad de Educación a Distancia y en Línea'),
    )

    nombre = models.CharField(max_length=60)
    facultad = models.CharField(max_length=30, choices=OPCIONES_FACULTAD)
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

class Tutoria(models.Model):
    OPCIONES_MODALIDAD = (
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
    )
    docente = models.ForeignKey(Persona, on_delete=models.CASCADE, to_field='cargo')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    horario=models.DateField()
    tema=models.CharField(max_length=60)
    modalidad=models.CharField(max_length=20, choices=OPCIONES_MODALIDAD)

    def info_tutoria(self):
        return "{} - {} - {}".format(self.docente, self.tema, self.modalidad)

    def __str__(self):
        return self.info_tutoria()

class Informe(models.Model):
    fecha=models.DateField()

class RegistroActividades(models.Model):
    fecha=models.DateField()

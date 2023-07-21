# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

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
        return "|{}|{}| periodo: {} hasta {}".format(self.nombre, self.facultad, self.inicio_periodo,
                                                     self.final_periodo)

    def __str__(self):
        return self.info_carrera()


class Docente(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, default=0)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    def info_docente(self):
        return "|{} {}| - {}".format(self.nombres, self.apellidos, self.carrera)

    def __str__(self):
        return self.info_docente()


class Asignatura(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, default=0)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, default=0)
    nombre = models.CharField(max_length=60)
    ciclo = models.CharField(max_length=20)
    paralelo = models.CharField(max_length=5)

    def info_asignatura(self):
        return "{} - {} - {} - {}".format(self.nombre, self.docente, self.ciclo, self.paralelo)

    def __str__(self):
        return self.info_asignatura()
        return self.info_asignatura()

'''class Tutoria(models.Model):
    OPCIONES_MODALIDAD = (
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
    )
    docente = models.ForeignKey(Docente, limit_choices_to={'cargo': 'docente'}, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    horario=models.DateTimeField()
    tema=models.CharField(max_length=60)
    modalidad=models.CharField(max_length=20, choices=OPCIONES_MODALIDAD)

    def info_tutoria(self):
        return "{} - {} - {}".format(self.docente, self.tema, self.modalidad)

    def __str__(self):
        return self.info_tutoria()'''


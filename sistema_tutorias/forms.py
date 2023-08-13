#from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass
#from django import forms

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model=Asignatura
        fields='__all__'

class CarreraForm(forms.ModelForm):
    class Meta:
        model=Carrera
        fields='__all__'

class DocenteForm(forms.ModelForm):
    class Meta:
        model=Docente
        fields='__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields=['nombre', 'apellido', 'usuario', 'clave', 'sexo', 'carrera', 'asignatura']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar las asignaturas basadas en la carrera seleccionada
        if self.instance and self.instance.carrera:
            self.fields['asignatura'].queryset = Asignatura.objects.filter(carrera=self.instance.carrera)

class TutoriaForm(forms.ModelForm):
    class Meta:
        model=Tutoria
        fields='__all__'


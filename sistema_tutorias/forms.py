from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class AsignaturaForm(ModelForm):
    class Meta:
        model=Asignatura
        fields='__all__'

class CarreraForm(ModelForm):
    class Meta:
        model=Carrera
        fields='__all__'

class DocenteForm(ModelForm):
    class Meta:
        model=Docente
        fields='__all__'


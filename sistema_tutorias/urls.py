from proyecto_tutorias.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('pedir_tutoria/', views.pedir_tutoria, name='pedir_tutoria')
]
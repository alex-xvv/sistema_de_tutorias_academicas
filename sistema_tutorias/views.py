from django.shortcuts import render


# Vistas de las diferentes paginas del proyecto.
def index(request):
    return render(request, 'html/index.html')


def about(request):
    return render(request, 'html/about.html')

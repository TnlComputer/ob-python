from django.shortcuts import render
from .models import Autor, Libro, LibroInstance, Gene


def index(request):
    num_libros = Libro.objects.all().count()
    num_instances = LibroInstance.objects.all().count()
    num_autors = Autor.objects.all().count()
    # num_genes = Gene.objects.all().count()

    disponibles = LibroInstance.objects.filter(status__exact='a').count()

    return render(
        request,
        'index.html',
        context={
            'num_libros': num_libros,
            'num_instances': num_instances,
            'num_autors': num_autors,
            'disponibles': disponibles,
            'demo': 'Soy Sandokan',
        })

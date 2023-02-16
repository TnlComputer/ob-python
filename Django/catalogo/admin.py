from django.contrib import admin
from .models import Autor, Gene, Libro, LibroInstance

admin.site.register(Autor)
admin.site.register(Gene)
admin.site.register(Libro)
admin.site.register(LibroInstance)

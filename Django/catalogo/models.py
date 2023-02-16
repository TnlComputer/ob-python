from django.db import models
from django.urls import reverse
import uuid


class Gene(models.Model):
    name = models.CharField(
        max_length=64, help_text="Pon el nombre del género")

    def __str__(self):
        return self.name


class Libro(models.Model):
    title = models.CharField(max_length=23)
    autor = models.ForeignKey("Autor", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=100, help_text="Pon aqui de que va el libro")
    isbn = models.CharField(
        max_length=13, help_text="El ISBN de 13 caracteres")
    gene = models.ManyToManyField(Gene)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('libro-detail', args=[str(self.id)])


class LibroInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Id unico para este libro")
    libro = models.ForeignKey('Libro', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=False)

    LOAN_STATUS = (
        ('m', 'Mantenimiento'),
        ('o', 'On loan'),
        ('a', 'Aviable'),
        ('r', 'Reserved')
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default='m', help_text='Disponibilidad del libro')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return '%s, %s' % (self.id, self.libro.title)


class Autor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("autor-detail", args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

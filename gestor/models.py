from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    # id = ObjectIdField()
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción de la categoría")
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

class Transaccion(models.Model):
    TIPO_TRANSACCION = {
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    }

    tipo = models.CharField(max_length=10, choices=TIPO_TRANSACCION, verbose_name="Tipo de transacción")
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Categoría"
    )
    monto = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Monto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    fecha = models.DateTimeField(default=timezone.now, verbose_name="Fecha")
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tipo} - {self.monto} - {self.fecha}"
    
    class Meta:
        verbose_name = "Transacción"
        verbose_name_plural = "Transacciones"
        ordering = ['-fecha', 'fecha_creacion']
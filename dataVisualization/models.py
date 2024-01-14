from django.db import models

# Create your models here.
class Sensor(models.Model):
    title = models.CharField(max_length=159, verbose_name='Título', null=True, default='Sin título')
    public = models.BooleanField(verbose_name='¿?Publicado', default=True)
    value = models.FloatField(verbose_name='Valor', null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado el")


    class Meta:
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Medicion(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='mediciones', null=True, blank=True, on_delete=models.CASCADE)
    valor = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Medición'
        verbose_name_plural = 'Mediciones'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.sensor.title} - {self.valor}"
from django.db import models

# Create your models here.
class Control(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
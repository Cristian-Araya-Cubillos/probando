from django.db import models

# Create your models here.
class contacto(models.Model):
    name = models.CharField(max_length=20)
    mensaje = models.CharField(max_length=30)
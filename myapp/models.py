from django.db import models

class Sancionatorio(models.Model):
    folio = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)

    def __str__(self):
        return self.folio

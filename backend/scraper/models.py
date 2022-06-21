from django.db import models

class GasStation(models.Model):
    _id = models.CharField(primary_key=True, max_length=255, default="")
    calle = models.CharField(max_length=255)
    rfc = models.CharField(max_length=255)
    date_insert = models.DateTimeField(null=True, blank=True)
    regular = models.TextField()
    colonia = models.CharField(max_length=255)
    numeropermiso = models.CharField(max_length=255)
    fechaaplicacion = models.CharField(max_length=255)
    permisoid = models.IntegerField()
    longitude = models.TextField()
    latitude = models.TextField()
    premium = models.TextField()
    razonsocial = models.CharField(max_length=255)
    codigopostal = models.TextField()
    dieasel = models.TextField()
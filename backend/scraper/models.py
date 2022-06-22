from django.db import models


class Station(models.Model):
    id = models.TextField(primary_key=True)
    calle = models.TextField(null=True)
    rfc = models.TextField(null=True)
    date_insert = models.DateTimeField(null=True)
    regular = models.FloatField(null=True)
    colonia = models.TextField(null=True)
    numeropermiso = models.TextField(null=True)
    fechaaplicacion = models.TextField(null=True)
    permisoid = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    premium = models.FloatField(null=True)
    razonsocial = models.TextField(null=True)
    codigopostal = models.TextField(null=True)
    dieasel = models.FloatField(null=True)
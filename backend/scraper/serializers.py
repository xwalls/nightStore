from scraper.models import Station
from rest_framework import serializers


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'rfc', 'razonsocial', 'latitude', 'longitude','premium', 'regular', 'dieasel', 'fechaaplicacion', 'permisoid', 'calle', 'colonia', 'numeropermiso', 'codigopostal']

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from scraper.models import GasStation
from django.core import serializers

# Create your views here.
def stations(request):
    stations = GasStation.objects.order_by('permisoid')[:5]
    stations_list = serializers.serialize('json', stations)
    return HttpResponse(stations_list, content_type="application/json")
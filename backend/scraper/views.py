from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from scraper.models import Station
from django.core import serializers
from .serializers import StationSerializer
from rest_framework import viewsets


class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer


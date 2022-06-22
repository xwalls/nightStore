from django.core.management.base import BaseCommand
from scraper.models import Station
import json


class Command(BaseCommand):
    help = 'Uses json to create data into DB'

    def handle(self, *args, **options):
        file_path = './data.json'
        with open(file_path) as json_file:
            data = json.load(json_file)
            rows = data['results']
            for row in rows:
                exists = Station.objects.filter(id=row['id']).exists()
                if not exists:
                    Station.objects.create(**row)

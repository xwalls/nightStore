from django.core.management.base import BaseCommand, CommandError
from scraper.models import GasStation
import json
from urllib import request
import requests


class Command(BaseCommand):
    help = 'Fetch and Update data from API'

    def handle(self, *args, **options):
        url = 'https://api.datos.gob.mx/v1/precio.gasolina.publico'
        page_size = get_total_page_size(url)
        new_url = url+'?pageSize='+page_size
        response = request.urlopen(new_url)

        data = json.loads(response.read().decode(encoding='utf-8-sig'))
        data_clean = json.dumps(data, ensure_ascii=False)
        data_clean = data_clean.replace('\ufeff','')
        data_json = json.loads(data_clean)
        rows = data_json['results']

        for row in rows:
            exists = GasStation.objects.filter(_id=row['_id']).exists()
            if not exists:
                GasStation.objects.create(**row)

    
def get_total_page_size(url) -> str:
    response = requests.get(url)
    page_size = response.json()['pagination']['total']
    return str(page_size)


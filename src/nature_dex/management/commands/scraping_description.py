# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import psycopg2
from urllib.request import urlretrieve
from urllib.error import HTTPError

from nature_dex.models import Specimen

# That command does web scraping from scientific name in wikipedia and saves the description

class Command(BaseCommand):
    args = ''
    help = 'Add description'

    def handle(self, *args, **options):
        self.add_description()


    def add_description(self):
        tot_counter = 0
        found_counter = 0
        specimenes = Specimen.objects.all()
        for s in specimenes:
            tot_counter += 1
            scientific_name = s.scientific_name.lower().replace(' ', '_')
            scientific_name = scientific_name.replace('-', '_')
            scientific_name = scientific_name.replace('/', '_')

            # Get common spanish name at Wikipedia
            url = "https://es.wikipedia.org/wiki/" + scientific_name
            url2 = "https://es.wikipedia.org/wiki/" + scientific_name.split('_')[0]

            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            all_p = soup.find_all("p")

            description = ""
            for p in all_p:
                description += str(p)

            if "Si el artículo aún así no existe" in description:
                print("No hay descripción para {}".format(scientific_name))
                scientific_name = scientific_name.split('_')[0]
                print("Probando con {}".format(scientific_name))

                response = requests.get(url2)
                soup = BeautifulSoup(response.text, "html.parser")

                all_p = soup.find_all("p")
                description = ""
                for p in all_p:
                    description += str(p)

                if "Si el artículo aún así no existe" in description:
                    print("Definitivamente, no hay descripción para {}".format(scientific_name))
                else:
                    description = description.replace('href="/wiki/', 'href="https://es.wikipedia.org/wiki/').replace('<a', '<a target="blank"')
                    s.identification = description
                    s.save()
                    print("Description saved for {}".format(scientific_name))
                    found_counter += 1
            else:
                description = description.replace('href="/wiki/', 'href="https://es.wikipedia.org/wiki/').replace('<a', '<a target="blank"')
                s.identification = description
                s.save()
                print("Description saved for {}".format(scientific_name))
                found_counter += 1

            print('Found: ' + str(found_counter) + ' of ' + str(tot_counter))


# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import psycopg2
from urllib.request import urlretrieve
from urllib.error import HTTPError
from nature_dex.settings.common import *

from nature_dex.models import Specimen


# That command does web scraping in bing from scientific name and saves the first image


class Command(BaseCommand):
    args = ''
    help = 'Add photo'

    def handle(self, *args, **options):
        self.add_photo()


    def add_photo(self):
        tot_counter = 0
        found_counter = 0
        specimenes = Specimen.objects.all()
        for s in specimenes:
            tot_counter += 1
            scientific_name = s.scientific_name.lower().replace(' ', '-')
            scientific_name = scientific_name.replace('/', '-')

            url = "http://www.bing.com/images/search?q=" + scientific_name
            url2 = "http://www.bing.com/images/search?q=" + scientific_name.split('-')[0]

            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            link = soup.find_all("a", class_="thumb")

            if link:
                image_url = link[0].get('href')
                filename = "{}.jpg".format(scientific_name)
                try:
                    urlretrieve(image_url, "{}/images/{}".format(MEDIA_ROOT, filename))
                    print("Image saved as {}".format(filename))
                    found_counter += 1
                except (HTTPError, UnicodeEncodeError) as e:
                    print("Error {}".format(e))
                    if len(link) > 1:
                        print("Probamos con otra imagen...")
                        image_url = link[1].get('href')
                        try:
                            urlretrieve(image_url, "{}/images/{}".format(MEDIA_ROOT, filename))
                            print("Image saved as {}".format(filename))
                            found_counter += 1
                        except (HTTPError, UnicodeEncodeError) as e:
                            print("Error {}".format(e))
                            if len(link) > 2:
                                print("Probamos con otra imagen...")
                                image_url = link[2].get('href')

                                try:
                                    urlretrieve(image_url, "{}/images/{}".format(MEDIA_ROOT, filename))
                                    print("Image saved as {}".format(filename))
                                    found_counter += 1
                                except (HTTPError, UnicodeEncodeError) as e:
                                    print("Error {}".format(e))
                                    print("Definitivamente, no hay imágen para {}".format(scientific_name))
                            else:
                                print("Definitivamente, no hay imágen para {}".format(scientific_name))
                    else:
                        print("Definitivamente, no hay imágen para {}".format(scientific_name))
            else:
                print("No hay imágen para {}".format(scientific_name))
                scientific_name = scientific_name.split('-')[0]
                print("Probando con {}".format(scientific_name))

                response = requests.get(url2)
                soup = BeautifulSoup(response.text, "html.parser")

                link = soup.find_all("a", class_="thumb")
                if link:
                    image_url = link[0].get('href')

                    filename = "{}.jpg".format(scientific_name)
                    try:
                        urlretrieve(image_url, "{}/images/{}".format(MEDIA_ROOT, filename))
                        print("Image saved as {}".format(filename))
                        found_counter += 1
                    except (HTTPError, UnicodeEncodeError) as e:
                        print("Error {}".format(e))
                        if len(link) > 1:
                            print("Probamos con otra imagen...")
                            image_url = link[1].get('href')

                            try:
                                urlretrieve(image_url, "{}/images/{}".format(MEDIA_ROOT, filename))
                                print("Image saved as {}".format(filename))
                                found_counter += 1
                            except (HTTPError, UnicodeEncodeError) as e:
                                print("Error {}".format(e))
                                if len(link) > 2:
                                    print("Probamos con otra imagen...")
                                    image_url = link[2].get('href')

                                    try:
                                        urlretrieve(image_url, "{}/images/{}".format(MEDIA_ROOT, filename))
                                        print("Image saved as {}".format(filename))
                                        found_counter += 1
                                    except (HTTPError, UnicodeEncodeError) as e:
                                        print("Error {}".format(e))
                                        print("Definitivamente, no hay imágen para {}".format(scientific_name))
                                else:
                                    print("Definitivamente, no hay imágen para {}".format(scientific_name))
                        else:
                            print("Definitivamente, no hay imágen para {}".format(scientific_name))
                else:
                    print("Definitivamente, no hay imágen para {}".format(scientific_name))

            print('Found: ' + str(found_counter) + ' of ' + str(tot_counter))


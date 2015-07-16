from django.core.management.base import BaseCommand
from nature_dex.models import Specimen
from bs4 import BeautifulSoup
import requests

class Command(BaseCommand):
    args = ''
    help = 'Add common name'

    def handle(self, *args, **options):
        self.add_common_name()

    def add_common_name(self):
        # Counters
        tot_counter = 0
        not_found_wm_counter = 0
        found_wm_counter = 0
        not_found_wp_counter = 0
        found_wp_counter = 0
        found_counter = 0

        # Obtain scientific names from db
        specimenes = Specimen.objects.all()
        for s in specimenes:
            specie = s.scientific_name
            spanish_name = ""
            tot_counter += 1
            print("=====================")

            # Get common spanish name at "Wikimedia Species"
            soup = self.beatifulSoup("https://species.wikimedia.org/wiki/", specie)
            res = soup.find("b", text="español:")
            spanish_wm_name = ""

            if res:
                spanish_wm_name = res.next_sibling
                found_wm_counter += 1
                found_counter += 1
                spanish_name = spanish_wm_name

            else:
                # Get common spanish name at Wikipedia
                not_found_wm_counter += 1
                spanish_wp_name = ""

                soup = self.beatifulSoup("https://es.wikipedia.org/wiki/", specie)
                res = soup.body.p.b
                res = soup.select("#mw-content-text")[0].children

                i = 0
                for child in res:
                    if (i == 2 or i == 4 or i==12) and child.name != "table" and not spanish_wp_name :
                        if "Wikipedia aún no tiene una página" not in str(soup.findAll("b")[0]):
                            dirty_spanish_wp_name = str(child.findAll("b")).capitalize()
                            # print("=="+dirty_spanish_wp_name)
                            spanish_wp_name = dirty_spanish_wp_name.replace('b>','').translate(str.maketrans('','','[</>]'))
                    i += 1

                if not res and "no tiene una página llamada" not in str(soup.findAll("b")[0]):
                    # "Not found" redirect at wikipedia. Example url: https://goo.gl/iF0pmo
                    #  Sometimes this other scrapping returns the valid common name from the top square of the web
                    res = list(soup.find("th", { "class" : "cabecera" }).children)[-1]
                    if res:
                        spanish_wp_name = res.string

                if not spanish_wp_name:
                    # No results found
                    not_found_wp_counter += 1
                    spanish_name = specie.strip().capitalize()
                else:
                    found_wp_counter += 1
                    if not spanish_wm_name:
                        spanish_name = spanish_wp_name
                        found_counter += 1

            s.common_name = spanish_name.strip().capitalize()
            s.save()
            print(specie + ": " + spanish_name.strip().capitalize())
            print('Found: ' + str(found_counter) + ' of ' + str(tot_counter))

        print("=============================================")
        print('Found at wikimedia: ' + str(found_wm_counter) + ' / Not found: ' + str(not_found_wm_counter))
        print('Found at wikipedia: ' + str(found_wp_counter) + ' / Not found: ' + str(not_found_wp_counter))


    def beatifulSoup(self, partial_url, specie):
        url = str(partial_url + specie)
        page = requests.get(url, allow_redirects=True)
        return BeautifulSoup(page.text, "html.parser")

# Obtain common names method from scientific names
# http://metodosdebusca.es/buscar-traduccion-de-nombres-de-plantas-animales-y-otros-seres-vivos/

# Wikimedia / Wikipedia API
# https://es.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=jsonfm&titles=Rattus%20norvegicuse)
# https://www.mediawiki.org/wiki/API:Query#Sample_query

# BeautifulSoup Doc
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#going-down

# Some controversial names for scrapping
# Upupa epops
# Anthus spinoletta
# Trachemys emolli
# Neovison vison
# Alytes obstetricans
# Lanius excubitor
# Anguilla anguilla
# Phoxinus phoxinus
# Nandayus nenday (OK 301)
# Mylabris nevadensis (Bad 301)
# Rana catesbeiana (BAD TRANSLATION)
# Acrocephalus melanopogon (UTF-8 problem)
# Oncorhynchus kisutch (Segundos resultados Wikipedia)
# Pipistrellus pipistrellus (P. pipistrellus, schreber, thomas, temminck)
# Falco_peregrinus (F. peregrinus)
# Anas crecca / Rattus norvegicus
# Linaria benitoi (Fail)

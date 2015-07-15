from bs4 import BeautifulSoup
import requests
import psycopg2
from urllib.request import urlretrieve
from urllib.error import HTTPError
from nature_dex.settings.common import *


# Obtain scientific names from db
con = psycopg2.connect(database='nature', user='')
cur = con.cursor()
cur.execute('select scientific_name from nature_dex_specimen')
rows = cur.fetchall()

# Counters
tot_counter = 0
found_counter = 0


for row in rows:
    tot_counter += 1
    scientific_name = row[0].lower().replace(' ', '_')
    scientific_name = scientific_name.replace('-', '_')
    scientific_name = scientific_name.replace('/', '_')

    # Get common spanish name at Wikipedia
    url = "https://es.wikipedia.org/wiki/" + scientific_name
    url2 = "https://es.wikipedia.org/wiki/" + scientific_name.split('-')[0]

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    description = soup.find_all("p")

    if description:
        print(description)
        print("Description saved for {}".format(scientific_name))
        found_counter += 1
    else:
        print("No hay descripción para {}".format(scientific_name))
        scientific_name = scientific_name.split('-')[0]
        print("Probando con {}".format(scientific_name))

        response = requests.get(url2)
        soup = BeautifulSoup(response.text, "html.parser")

        description = soup.find_all("p")
        if description:
            print(description)
            print("Description saved for {}".format(scientific_name))
            found_counter += 1
        else:
            print("Definitivamente, no hay descripción para {}".format(scientific_name))

    print('Found: ' + str(found_counter) + ' of ' + str(tot_counter))




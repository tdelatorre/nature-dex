from bs4 import BeautifulSoup
import requests
import psycopg2
from urllib.request import urlretrieve
from nature_dex.settings.common import *


# Obtain scientific names from db
con = psycopg2.connect(database='nature', user='')
cur = con.cursor()
cur.execute('select scientific_name from nature_dex_specimen')
rows = cur.fetchall()

for row in rows:
    scientific_name = row[0].lower().replace(' ', '-')
    #~ url = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + scientific_name + "&start=1"

    url = "http://www.bing.com/images/search?q=" + scientific_name

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    link = soup.find("a", class_="thumb")
    if link:
        image_url = link.get('href')
        filename = "{}.jpg".format(scientific_name)
        urlretrieve(image_url, "{}/images/{}".format(MEDIA_ROOT, filename))
        # TODO: Queda guardarlo en la base de datos y asociarlo al fichero guardado.
        print("Image saved as {}".format(filename))
    else:
        print("No hay imágen para {}".format(scientific_name))
        scientific_name = scientific_name.split('-')[0]
        print("Probando con {}".format(scientific_name.split('-')[0]))

        url = "http://www.bing.com/images/search?q=" + scientific_name

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        link = soup.find("a", class_="thumb")
        if link:
            image_url = link.get('href')
            filename = "{}.jpg".format(scientific_name)
            urlretrieve(image_url, "{}/images/{}".format(MEDIA_ROOT, filename))
            # TODO: Queda guardarlo en la base de datos y asociarlo al fichero guardado.
            print("Image saved as {}".format(filename))
        else:
            print("Definitivamente, no hay imágen para {}".format(scientific_name))
            print("Creando fichero specimenes-without-photo.txt")
            # TODO: Creas fichero para meter los nombres científicos que no tengan foto.





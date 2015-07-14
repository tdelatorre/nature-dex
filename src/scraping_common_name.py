from bs4 import BeautifulSoup
import requests
import psycopg2
import sys

# Obtain scientific names from db
con = psycopg2.connect(database='nature', user='')
cur = con.cursor()
cur.execute('select scientific_name from nature_dex_specimen')
rows = cur.fetchall()

# Counters
tot_counter = 0
not_found_wm_counter = 0
found_wm_counter = 0
not_found_wp_counter = 0
found_wp_counter = 0
found_counter = 0

for row in rows:
    specie = row[0]
    tot_counter = tot_counter + 1
    print()
    print(specie)

    # Get common spanish name at Wikimedia Species
    url = "https://species.wikimedia.org/wiki/" + specie
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    res = soup.find("b", text="español:")
    if res:
        spanish_wm_name = res.next_sibling
    else:
        spanish_wm_name = ""
        res = soup.find("b", text="English:")
        # Trying to translate the common english name from Wikimedia
        if res:
            english_name = res.next_sibling
            url = "https://translate.google.com/translate_a/single?client=t&sl=en&tl=es&dt=t&dt=at&ie=UTF-8&q="+english_name
            page = requests.get(url)
            spanish_wm_name = str(page.content).split('"')[1]
        else:
            spanish_wm_name = ""

    if not spanish_wm_name:
        print("Wikimedia: No existen resultados")
        not_found_wm_counter = not_found_wm_counter +1
    else:
        print("Wikimedia: " + spanish_wm_name)
        found_wm_counter = found_wm_counter + 1
        found_counter = found_counter + 1

    # Get common spanish name at Wikipedia
    url = "https://es.wikipedia.org/wiki/" + specie
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    res = soup.p.b
    # sometimes this other scrapping returns the valid common name from the top square of the web
    # res = list(soup.find("th", { "class" : "cabecera" }).children)[-1]

    if res:
        spanish_wp_name = res.string
    else:
        spanish_wp_name = ""

    if not spanish_wp_name:
        print("Wikipedia: No existen resultados")
        not_found_wp_counter = not_found_wp_counter +1
    else:
        print("wikipedia: " + spanish_wp_name)
        found_wp_counter = found_wp_counter + 1
        if not spanish_wm_name:
            found_counter = found_counter + 1

    print("Found: " + str(found_counter) + " of " + str(tot_counter))

print("=============================================")
print("Found at wikimedia: " + found_wm_counter + "from" + not_found_wm_counter)
print("Found at wikipedia: " + found_wp_counter + "from" + not_found_wp_counter)



# Obtain common names method from scientific names
# http://metodosdebusca.es/buscar-traduccion-de-nombres-de-plantas-animales-y-otros-seres-vivos/

# Wikimedia / Wikipedia API
# https://es.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=jsonfm&titles=Rattus%20norvegicuse)
# https://www.mediawiki.org/wiki/API:Query#Sample_query

# BeautifulSoup Doc
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#going-down

# specie = "Crocodylus niloticus"
# specie = "Rattus norvegicus"
# specie = "Agabus paludosus"
# specie = "Cuculus canorus"
# specie = "Quercus falcata"
# specie = "Salmo trutta"















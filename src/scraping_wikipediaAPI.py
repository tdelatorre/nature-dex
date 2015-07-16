from bs4 import BeautifulSoup
import requests
import psycopg2
import json


def find_between(s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def findall(v, k):
    res = None
    if type(v) == type({}):
        for k1 in v:
            if k1 == k:
                res = v[k1]
                # print(res)
            else:
                res = findall(v[k1], k)
    return res

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

# for row in rows:
#     specie = row[0]
for row in rows[:1]:
    specie = "Rattus norvegicus"
    print("=======================")
    print("  \""+specie+"\"")
    print("=======================")

    # SOUP Way
    # url = "https://es.wikipedia.org/w/api.php?action=query&titles=" + specie + "&prop=revisions&rvprop=content&format=xml"
    # print(url)
    # page = requests.get(url, allow_redirects=True)
    # soup = BeautifulSoup(page.text, "html.parser")
    # print(soup)

    # JSON Way
    url = "https://es.wikipedia.org/w/api.php?action=query&titles="+ specie + "&prop=revisions&rvprop=content&redirects&converttitles&format=json"
    # print(url)
    page = requests.get(url, allow_redirects=True)
    json =page.json()
    # print(json["query"]["pages"])


    # Getting name from wikipedia API
    revisions_list = findall(json, 'revisions')
    if revisions_list:
        revisions_json = revisions_list[0]
        content = revisions_json['*']
        print(find_between(content, "| name = ", "\n" ).replace("''", ""))

    # Getting description from wikipedia API
    url = "https://es.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=&explaintext=&&format=json&rvprop=content&redirects&titles="+ specie
    # print(url)
    page = requests.get(url, allow_redirects=True)
    json =page.json()
    print(findall(json, "extract"))

#For descriptions
#https://es.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=&explaintext=&&format=json&rvprop=content&titles=Montifringilla%20nivalis&redirects

#Redirects & converttitles
# https://es.wikipedia.org/w/api.php?action=query&titles=Montifringilla nivalis&prop=revisions&rvprop=content&redirects&converttitles&format=json
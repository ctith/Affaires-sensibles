import requests
from bs4 import BeautifulSoup
import re

# structure de la page html
#url = "https://podcloud.fr/podcast/affaires-sensibles"

# Recupere reponse HTTP GET du site
#r = requests.get(url)

# fichier output liens a telecharger
f = open("liens mp3 affaires sensibles.txt", "w")
html = open("affaires_sensibles.html","r", encoding="utf8")
html = html.read()
print(html)
# transformer html en dom
dom = BeautifulSoup(html,"html.parser")

# recuperer ligne html qui nous interesse
liensHTML = dom.find_all(href=re.compile("https://podcloud.fr/ext/affaires-sensibles/"))

# recuperer info dans le bloc html qui nous interesse
for liens in liensHTML:
    liensCourts = str(liens.get('href'))
    liensCourts = liensCourts.replace("?p=dl","")+ '\n'
    f.write(liensCourts)

f.close()
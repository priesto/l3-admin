#! /usr/bin/env python

import requests
import json
import subprocess
from bs4 import BeautifulSoup

# Récupération de la page HTML.
req = requests.get('https://www.cert.ssi.gouv.fr')
soup = BeautifulSoup(req.content, 'lxml')

# On se place à un endroit plus proche des informations que l'on souhaite récupérer.
soup = soup.find('div', {'class': 'items-list'})
soup = soup.find('div')

# Récupération des données qui nous intéresse.
date = soup.find('div').find('span').text
code = soup.findAll('div')[1].find('span').find('a').text
title = soup.findAll('div')[2].find('span').find('a').text

# Dictionnaire contenant nos données.
json_object = {'date': date, 'code': code, 'title': title}

# Ecriture des données au JSON dans le fichier `alertes.json`.
with open('../alertes.json', 'w') as f:
    json.dump(json_object, f)

# Appel du moteur chargé de stocker les alertes
subprocess.Popen("python ../StockageCollecte/m_alertes.py", shell=True)
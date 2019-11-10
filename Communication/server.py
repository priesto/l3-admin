#! /usr/bin/env python
# coding: utf-8

from flask import Flask
from flask import request
import json
import subprocess

app = Flask('app')

# Permet d'attraper les requêtes de type POST vers la racine '/'
@app.route("/", methods=['POST'])
def main():
    # Récupération des données
    body = json.loads(request.json)
    # Ecriture dans le fichier data.json
    with open('../data.json', 'w') as f:
        json.dump(body, f)

    # Appel vers le moteur chargé de stocker les sondes
    subprocess.Popen("python ../StockageCollecte/moteur.py", shell=True)
    # On répond à la requête.
    return 'OK'

app.run(host='0.0.0.0')
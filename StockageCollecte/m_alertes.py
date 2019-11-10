#! /usr/bin/env python
# coding: utf-8

import sqlite3
import json
import time

# Connexion vers la base de donnée.
conn = sqlite3.connect('../database.db')
cursor = conn.cursor()

# Création de la table si celle-ci n'existe pas.
cursor.execute("""
	CREATE TABLE IF NOT EXISTS alertes (
		ref VARCHAR(50) PRIMARY KEY UNIQUE,
		titre VARCHAR(120) NOT NULL,
		date_alerte TEXT NOT NULL,
		date_insertion TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
	)
""")

# Chargement du fichier contenant les alertes.
alerte = json.load(open('../alertes.json'))

# Insertion au sein de la base de donnée.
cursor.execute("INSERT INTO alertes (ref, titre, date_alerte, date_insertion) VALUES (?,?,?,?)", (alerte['code'], alerte['title'], alerte['date'], time.strftime('%Y-%m-%d %H:%M:%S')))
conn.commit()
conn.close()


# Sauvegarde des données
subprocess.Popen("bash ../StockageCollecte/Backup/backup.sh", shell=True)
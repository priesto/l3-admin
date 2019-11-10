#! /usr/bin/env python
# coding: utf-8

import subprocess
import sqlite3
import json
import time

# Connexion vers la base de donnée
conn = sqlite3.connect('../database.db')
cursor = conn.cursor()

# Création de la table si celle-ci n'existe pas
cursor.execute("""
	CREATE TABLE IF NOT EXISTS sondes (
		mid VARCHAR(40) NOT NULL,
		cpu INTEGER NOT NULL,
		disk INTEGER NOT NULL,
		memory INTEGER NOT NULL,
		uptime TEXT NOT NULL,
		hostname VARCHAR(50) NOT NULL,
		ip_address VARCHAR(30) NOT NULL,
		nb_processus INTEGER NOT NULL,
		nb_utilisateurs INTEGER NOT NULL,
		date_insertion TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
	)
""")

# Récupération des données envoyées par les sondes, puis insertion au sein de la base de donnée.
with open('../data.json') as json_file:
	data = json.load(json_file)
	cursor.execute("INSERT INTO sondes (mid, hostname, uptime, nb_utilisateurs, memory, nb_processus, disk, cpu, ip_address, date_insertion) VALUES (?,?,?,?,?,?,?,?,?,?)", (data['mid'], data['hostName'], data['uptime'], data['nbUsers'], data['memory'], data['nbProcess'], data['diskUsage'], data['cpu'], data['ip'], time.strftime('%Y-%m-%d %H:%M:%S')))
	conn.commit()
	conn.close()


# Permet de créer une sauvegarde après insertion des données.
subprocess.Popen("bash ../StockageCollecte/Backup/backup.sh", shell=True)
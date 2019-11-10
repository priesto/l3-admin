#! /usr/bin/env python
# coding: utf-8

import sqlite3
import datetime
import pygal
import json
import subprocess
import string



# Récupération des données de situation de crise

file = open('./config.dat', 'r').readlines()

# On parse chaque valeur en un entier
max_mem = int(file[0])
max_cpu = int(file[1])
max_disk = int(file[2])









# Affichage des données récentes sur le terminal

conn = sqlite3.connect('../database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM sondes GROUP BY mid')

data = cursor.fetchall()

for i in data:
	print('Machine : %s' % i[0])
	print('\tNom : %s' % i[5])
	print('\tIP : %s' % i[6])
	print('\tNombre utlisateurs : %s' % i[8])
	print('\tAllumée depuis : %s' % str(i[4]))
	print('\tNombre processus : %d' % i[7])
	print('\tUtilisation CPU: %d%%' % i[1])
	print('\tUtilisation DISQUE: %d%%' % i[2])
	print('\tUtilisation MEMOIRE: %d%%' % i[3])
	print
	





# Détection de crise

for i in data:
	if i[1] > max_cpu:
		subprocess.Popen("bash ./alerte_cpu.sh", shell=True)
	if i[2] > max_disk:
		subprocess.Popen("bash ./alerte_disk.sh", shell=True)
	if i[3] > max_mem:
		subprocess.Popen("bash ./alerte_mem.sh", shell=True)
	








# Afficher sous forme de graphe les données avec historique.
	
# Pour récupérer les résultats sous forme de tableau d'élément et non de tuple
conn.row_factory = lambda cursor, row: row[0]

cursor = conn.cursor()

# On récupère les différents mid (indentifiant de machine)
cursor.execute('select mid from sondes group by mid')

for i in cursor.fetchall():
	# Pour chaque machine, on récupère cpu, disque, mémoire et date
	sql = 'select cpu from sondes where mid = ?'
	cursor.execute(sql, (i,))
	cpu = cursor.fetchall()

	sql = 'select disk from sondes where mid = ?'
	cursor.execute(sql, (i,))
	disk = cursor.fetchall()

	sql = 'select memory from sondes where mid = ?'
	cursor.execute(sql, (i,))
	memory = cursor.fetchall()

	sql = 'select date_insertion from sondes where mid = ?'
	cursor.execute(sql, (i,))
	d = cursor.fetchall()


	# On utilise pygal pour créer le graphe
	date_chart = pygal.Line()
	date_chart.title = "Graphe evolution pour machine : " + str(i)
	date_chart.x_labels = d
	date_chart.add("Memoire", memory)
	date_chart.add("Disque", disk)
	date_chart.add("Processeur", cpu)
	#date_chart.render_in_browser()
	date_chart.render_to_file('/tmp/' + str(i) + '.svg')
	subprocess.Popen(['gvfs-open', '/tmp/' + str(i) + '.svg'])



conn.row_factory = None
cursor = conn.cursor()













# Dernière communication

cursor.execute('select distinct date_insertion from sondes order by date_insertion limit 1')
last_com = cursor.fetchall()[0]
last_com = json.dumps(last_com[0]).replace('"', '')

print "Dernière connexion : " + last_com
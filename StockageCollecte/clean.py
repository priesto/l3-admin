#! /usr/bin/env python
# coding: utf-8


from datetime import datetime
import sqlite3

# Connexion à la base.
conn = sqlite3.connect('../database.db')
cursor = conn.cursor()


###### Nettoyage de la table sondes

# Récupération de toute les sondes stockées dans la base de donnée.
cursor.execute('select * from sondes')

for i in cursor.fetchall():
    # On parse la chaîne représentant date en objet date.
    date = datetime.strptime(i[9], '%Y-%m-%d %H:%M:%S')
    delta = datetime.now() - date

    # Si différence entre maintenant et notre date > 30
    if delta.days > 30 :
        # Supprimer cette entrée, car trop ancienne
        sql = 'delete from sondes where mid = ? and date_insertion = ?'
        cursor.execute(sql, (i[0], i[9],))
        conn.commit()

    
##### Nettoyage de la table alertes

# Récupération de toute les alertes.
cursor.execute('select * from alertes')

for i in cursor.fetchall():
    # On parse la chaîne représentant date en objet date.    
    date = datetime.strptime(i[3], '%Y-%m-%d %H:%M:%S')
    delta = datetime.now() - date

    # Si différence entre maintenant et notre date > 30
    if delta.days > 30 :
        # Supprimer cette entrée, car trop ancienne
        sql = 'delete from alertes where ref = ? and date_insertion = ?'
        cursor.execute(sql, (i[0], i[3],))
        conn.commit()


conn.close()
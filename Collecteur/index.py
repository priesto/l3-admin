#! /usr/bin/env python

import requests
import json
import os


from users import nb_users
from host import hostname
from processes import nb_process
from uptime import d


# Récupération des données de chaque script.
disk_usage = os.popen('bash Mixte/disk.sh').read().strip()
mem_available = os.popen('bash mem.sh').read().strip()
cpu_usage = os.popen('bash cpu.sh').read().strip()
ip_address = os.popen('bash ip.sh').read().strip()
mid = open('/etc/machine-id').read().strip()


# Insertion des données dans un dictionnaire
json_object = {
	'hostName': hostname,
	'nbUsers': nb_users,
	'uptime': d,
	'nbProcess': nb_process,
	'diskUsage': disk_usage,
	'memory': mem_available,
	'cpu': cpu_usage,
	'ip': ip_address,
	'mid': mid
}

# Utilisation de json.dumps pour créer un chaîne de charactère au format JSON.
j = json.dumps(json_object)

# Transmission des données JSON au serveur
req = requests.post('http://192.168.0.16:5000', json=j)
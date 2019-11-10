#! /bin/bash

# installe python et pip
sudo apt-get update
sudo apt-get -y install install python python-pip

# installe les packages nécessaires
sudo pip install --upgrade pip
sudo pip install --user pipenv
sudo pip install psutil
sudo pipenv install requests

# création de la tâche cron
crontab -l > cron
echo "*/5 * * * * python index.py" >> cron 
crontab cron
rm cron
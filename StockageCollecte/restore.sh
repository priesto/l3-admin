#! /bin/bash

cd /home/harik/Documents/cours/L3/AdminSys/Projet

rm database.db
sqlite3 database.db < StockageCollecte/Backup/backup_file.db
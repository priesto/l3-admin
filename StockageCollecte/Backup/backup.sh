#! /bin/bash

cd /home/harik/Documents/cours/L3/AdminSys/Projet

sqlite3  database.db ".backup 'backup_file.db'"
mv backup_file.db StockageCollecte/Backup
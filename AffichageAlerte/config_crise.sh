#! /bin/bash

read -p 'Pourcentage max de mémoire à ne pas dépasser : ' mem
read -p 'Pourcentage max de cpu à ne pas dépasser : ' cpu
read -p 'Pourcentage max de disque à ne pas dépasser : ' disk

# Permet de vider le fichier.
> config.dat

echo $mem >> config.dat
echo $cpu >> config.dat
echo $disk >> config.dat
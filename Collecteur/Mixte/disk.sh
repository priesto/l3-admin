#! /bin/bash

df / | awk '{print $5}' | ./Mixte/disk.py

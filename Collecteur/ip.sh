#! /bin/bash

ip=$(ifconfig | grep -A1 ^enp | awk '{print $2}' | tail -n1 | cut -d ':' -f2)

echo $ip
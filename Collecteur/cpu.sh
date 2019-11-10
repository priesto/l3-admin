#! /bin/bash

# https://stackoverflow.com/questions/9229333/how-to-get-overall-cpu-usage-e-g-57-on-linux/9229580#9229580
# https://stackoverflow.com/a/9229580/7197135

cpu_count=$(grep 'processor' /proc/cpuinfo | wc -l)
total_cpu_usage=$(top -bn1 | awk '{print $9}' | tail -n+8 | awk '{s+=$1} END {print s}')

echo "$total_cpu_usage/$cpu_count" | bc
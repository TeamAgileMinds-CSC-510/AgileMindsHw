#!/bin/bash
awk -F',' 'NR>1 && $3==2 && $13~"S"' titanic.csv | sed 's/female/F/g; s/male/M/g' | awk -F',' '{sum += $7; count++} END {if (count > 0) print sum / count}'
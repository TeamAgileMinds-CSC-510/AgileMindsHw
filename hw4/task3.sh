#!/bin/bash
result=$(awk -F',' 'NR>1 && $3==2 && $13~"S"' titanic.csv | sed 's/female/F/g; s/male/M/g')

echo "$result"

echo "$result" | awk -F',' '{sum += $7; count++} END {if (count > 0) print "Average Age: " sum / count}'


#!/bin/bash
result=$(gawk -F',' 'NR>1 && $3==2 && $NF ~ /S/' titanic.csv | sed 's/female/F/g; s/male/M/g')

echo "$result"

echo "$result" | gawk -F, '$(NF-6) != "" { sum += $(NF-6); count++ } END { if (count > 0) print "\nAverage Age:", sum/count; else print "No Age data found." }'
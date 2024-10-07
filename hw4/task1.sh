#!/bin/bash
# Finds and kills the process running infinite.sh
pids=$(pgrep -f 'bash infinite.sh')
if [ ! -z "$pids" ]; then
    for pid in $pids; do
        echo "Killing process with ID: $pid "
        kill $pid #
        echo " $pid has been killed."
    done
else
    echo "No process found."
fi
#!/bin/bash
pids=$(pgrep -f 'infinite.sh')

if [ ! -z "$pids" ]; then
    echo "$pids" | xargs -r -n 1 sh -c 'echo "Killing process with ID: $0"; kill "$0" && echo "$0 has been killed." || echo "Failed to kill process $0."'
else
    echo "No process found."
fi
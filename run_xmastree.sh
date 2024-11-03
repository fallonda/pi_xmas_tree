#!/bin/bash

# Runs the led xmas lights and countdown timer to christmas as two separate python jobs.
sleep 10
python3 /home/pi/pi_xmas_tree/src/xmastree.py &
sleep 30
python3 /home/pi/pi_xmas_tree/src/display_days.py &

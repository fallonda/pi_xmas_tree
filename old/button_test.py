#!/usr/bin/env python3

import RPi.GPIO as io
from time import sleep
io.setmode(io.BCM)
io.setwarnings(False)
button1, button2 = 17, 12
io.setup([button1,button2], io.IN)

counter = 0
try:
  while True:
    print(f"b1: {io.input(button1)}. b2: {io.input(button2)}. counter: {counter}.")
    sleep(0.1)
    counter += 1
except KeyboardInterrupt:
  pass

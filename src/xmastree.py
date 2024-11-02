#!/usr/bin/env python3

# Script to run xmastree lights

# Environment setup
import RPi.GPIO as io
from time import sleep
import random
from datetime import datetime

# Pin setup
io.setmode(io.BCM)
io.setwarnings(False)
pin_list = [2,3,4,18,27,22,21,20,16,19,13,6,5]
io.setup(pin_list, io.OUT, initial=0) # Set all channels to out.
led_dict = {
  "white": [19],
  "green": [2,4,13],
  "red": [3,22,16],
  "blue": [18,27,20],
  "rgb": [21,6,5]
}
white_and_rgb = []
for col in ["white", "rgb"]:
  white_and_rgb.extend(led_dict[col])
colours_only = []
for col in ["red", "green", "blue"]:
  colours_only.extend(led_dict[col])

class Bulb(io.PWM):
    """Led that will be controlled by PWM"""
    def __init__(self, pin):
        self.pin = pin
        super().__init__(pin, 100) # channel and freq (Hz)
        self.cycle_value = 0
        self.cycle_target = random.randint(0,100)
        self.start(self.cycle_value)

    def update(self):
        """Increase or decrease the duty cycle towards the target

        Changes the unit if necessary, then updates the duty cycle
        with the new value."""
        if self.cycle_value > self.cycle_target:
            self.cycle_value -= 1
        elif self.cycle_value < self.cycle_target:
            self.cycle_value += 1
        else: # If equal, choose new target
            self.cycle_target = random.randint(0,100)
        self.ChangeDutyCycle(self.cycle_value)

    def set_max(self):
        """Set values to 100"""
        self.cycle_value = 100

list_of_bulbs = [Bulb(pin) for pin in colours_only]

time_slice = 0.01

# Main
try:
  while True:
    # Turn on the white and rgb.
    io.output(white_and_rgb, 1)
    # Turn on the pwm controlled leds. 
    for bulb in list_of_bulbs:
      bulb.update()
    sleep(time_slice)

except KeyboardInterrupt:
    # Turn off all bulbs
    io.output(pin_list, 0)
    for bulb in list_of_bulbs:
        bulb.stop()

# End.




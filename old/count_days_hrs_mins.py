#!/usr/bin/env python3

# Script to run xmastree lights and the countdown to Christmas

# Environment setup
from time import sleep
import ZeroSeg.led as seg
import random
from datetime import datetime

# Setup segment display
device_scroll = seg.sevensegment(cascaded=2)
device_static = seg.sevensegment()

messages = [
  "TIS THE SEASON",
  "HAPPY HOLIDAYS",
  "HO HO HO",
  "NOLLAIG",
  "NOEL NOEL NOEL",
]
xmas = datetime.strptime("2023-12-25 00:00:00", "%Y-%m-%d %H:%M:%S")

def buffer_digit(input_digit):
    """Put a zero infront of a digit if it is only a single digit"""
    if len(str(input_digit)) == 1:
        output_digit = "0" + str(input_digit)
    elif len(str(input_digit)) == 2:
        output_digit = str(input_digit)
    else:
        raise ValueError(f"length of input_digit '{input_digit}' was not 1 or 2.")
    return output_digit

def countdown_display(device, deviceId, dot_on):
  """Write the digits to the display"""
  time_until_xmas = xmas - datetime.now()
  days = buffer_digit(time_until_xmas.days)
  hours = buffer_digit(int(time_until_xmas.seconds / 3600))
  mins = buffer_digit(int(time_until_xmas.seconds % 3600 / 60))
  device.letter(deviceId, 8, days[0])
  device.letter(deviceId, 7, days[1])
  device.letter(deviceId, 6, "-")
  device.letter(deviceId, 5, hours[0])
  device.letter(deviceId, 4, hours[1])
  device.letter(deviceId, 3, "-")
  device.letter(deviceId, 2, mins[0])
  device.letter(deviceId, 1, mins[1], dot_on)

counter_for_message = 0

# Main
try:
  while True:
    # Start countdown display
    countdown_display(device_static, 0, False)
    sleep(1)
    countdown_display(device_static, 0, True)
    sleep(1)
    counter_for_message += 2
    if counter_for_message > 180:
      device_scroll.show_message(random.choice(messages), delay = 0.2)
      counter_for_message = 0

except KeyboardInterrupt:
    device_scroll.clear()
    device_static.clear()

# End.




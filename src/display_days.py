#!/usr/bin/env python3

# Script to run countdown to Christmas Day on the 7-seg display. 
# Output will be e.g. "123 DAYS"

from time import sleep
import ZeroSeg.led as seg
import random
from datetime import date
from utils import get_days_to_xmas, buffer_digit

SEC_BETWEEN_SCROLLING_MESSAGE = 60

# Setup segment display
device_scroll = seg.sevensegment(cascaded=2)
device_static = seg.sevensegment()

messages = [
  "TIS THE SEASON",
  "HAPPY HOLIDAYS",
  "HO HO HO",
  "NOEL NOEL NOEL",
  "SANTA STOP HERE",
  "ROWAN IS ON THE GOOD LIST",
  "JINGLE BELLS",
  "LYNN IS THE BEST MOM"
]

def show_days_message(device, deviceId, days: str, dot_on: bool):
    """Write to 7-seg with e.g. '123 days'"""
    message_str = days + " days"
    # Fill the first 7 positions.
    # Display position is ordered 1-8 right to left. 
    for i in range(7):
        device.letter(deviceId, 8-i, message_str[i])
    # For the last position (RHS, 1), add option for turning on the dot.
    device.letter(deviceId, 1, message_str[7], dot_on)

# Main loop
counter_for_intermittent_message = 0
try:
    while True:
        days_to_xmas = get_days_to_xmas(date.today())
        buffer_days_to_xmas = buffer_digit(days_to_xmas)
        show_days_message(device_static, 0, buffer_days_to_xmas, False)
        sleep(1)
        show_days_message(device_static, 0, buffer_days_to_xmas, True)
        sleep(1)
        counter_for_intermittent_message += 2 # 2 sec passed
        if counter_for_intermittent_message >= SEC_BETWEEN_SCROLLING_MESSAGE:
            device_scroll.show_message(random.choice(messages), delay = 0.2)
            counter_for_intermittent_message = 0

except KeyboardInterrupt:
    device_scroll.clear()
    device_static.clear()

finally:
    device_scroll.clear()
    device_static.clear()
    
# End.

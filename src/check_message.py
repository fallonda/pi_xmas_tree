#!/usr/bin/env python3

from time import sleep
import ZeroSeg.led as seg

# Setup segment display
device_scroll = seg.sevensegment(cascaded=2)
device_static = seg.sevensegment()

test_message = "OUR LITTLE BOY IS ON THE NICE LIST"

device_scroll.show_message(test_message, delay = 0.2)

# End.

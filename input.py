#!/usr/bin/env python

import sys
from evdev import InputDevice, categorize, ecodes
import requests

if len(sys.argv) < 2:
    sys.exit("Please enter a device number")

devid = sys.argv[1]
device = "/dev/input/event" + devid
device = InputDevice(device)

full_code = ""
print("Listening to input on device " + devid)

for event in device.read_loop():
    if event.type == ecodes.EV_KEY and event.value == 1:
	if event.code != ecodes.KEY_ENTER:
	    full_code += ecodes.KEY[event.code][4:]
	else:
	    print("Read code " + full_code + " on device " + devid)
	    r = requests.post('http://192.168.86.40:5000/play', json={"code": full_code, "device": devid})
	    #r = requests.get('http://192.168.86.40:5000')
	    full_code = ""


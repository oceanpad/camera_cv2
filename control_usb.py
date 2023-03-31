import usb.core
import usb

# dev = usb.core.find(idVender=1, idProduct=2)

#print(dev)

#if dev is None:
#  raise ValueError('Device not found')

# dev.setconfiguration()

# dev.reset()

busses = usb.busses()
for bus in busses:
  devices = bus.devices
  for dev in devices:
    print("-"*20)
    print(dev.iManufacturer)
    print(dev.usbVersion)
    print("  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor))
    print("  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct))
    print("Manufacturer:", dev.iManufacturer)
    print("Serial:", dev.iSerialNumber)
    print("Product:", dev.iProduct)

import time 
import usb.core 
import usb.util
from sys import exit
import sys

VID = 0x04d8
PID = 0x000
dev = usb.core.find(idVendor=VID, idProduct=PID)
if not dev:
  print("Could not find device ")
  exit(1)
else:
  print("Yeeha! Found the device")

dev.set_configuration()

# command : Limit
dev.write(2, (0x59, 0x4c, 0x0d))


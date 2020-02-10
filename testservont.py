# test no threading 
from rpiHAT import ServoNT
import time

s=ServoNT(channel=1, freq=98.1)
s.set(0.1)
while True:
  time.sleep(0.5)
  try:
    pass
  except (KeyboardInterrupt, SystemExit):
    s.set(0.15)
    

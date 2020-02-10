# test no threading 
from rpiHAT import ServoNT
import time

s=ServoNT(channel=1, freq=98.1)
s.pulse(0.1)
while True:
  time.sleep(0.5)
  try:
    pass
  except (KeyboardInterrupt, SystemExit):
    s.pulse(0.15)
    

# test no threading 
from rpiHAT import ServoNT
import time

s=ServoNT(channel=1, freq=92.7)
s.pulse(0.1)

try:
    while True:
        time.sleep(0.5)
except (KeyboardInterrupt, SystemExit):
    s.pulse(0.15)

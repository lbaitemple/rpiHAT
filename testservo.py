#from rpiHAT.clock import clock
#from rpiHAT.servo import servo
from rpiHAT import Servo
from rpiHAT import Clock

t= Servo(1)
clck = Clock(t, 1)
clck.start()


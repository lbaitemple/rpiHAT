from rpiHAT.altimu import AltIMU
from rpiHAT.servo import *
from  rpiHAT.clock import Clock
from rpiHAT.RotaryEncoder import RotaryEncoder
#from .altimu import *
#from .servo import servo
#from .clock import clock 

# constants
IDLE = 0
RUNNING = 1
PAUSED = 2
EXITING = 3

# idle function
def idle():
    set_state(IDLE)

# run function
def run():
    set_state(RUNNING)

# pause function
def pause():
    set_state(PAUSED)

# exit function
def exit():
    set_state(EXITING)

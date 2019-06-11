from datetime import datetime
from time import sleep

from rpiHAT import AltIMU

def callimu():
    imu = AltIMU()
    imu.enable()

    imu.calibrateGyroAngles()
    start = datetime.now()
    imu.initComplementaryFromAccel=True
    imu.initKalmanFromAccel = True
    while True:
        stop = datetime.now() - start
        start = datetime.now()
        deltaT = stop.microseconds/1000000.0
        print("Gyro:", imu.getComplementaryAngles(deltaT = deltaT))
        print("Accelerometer (G):", imu.getAccInG())
        sleep(1)


if __name__ == '__main__':
    callimu()

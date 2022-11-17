import sys
import os
import datetime

class CarParkingLogger:
    def __init__(self, dateTime = 'ok'):
        self.dateTime = dateTime

    def check_in(self, license_plate, dateTime):
        ...

    def check_out(self, license_plate, dateTime):
        ...   

if __name__ == "__main__":
    parkingMachine = CarParkingLogger()

    print(parkingMachine.dateTime)
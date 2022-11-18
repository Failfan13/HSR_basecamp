import sys
import os
import datetime
import re

class CarParkingLogger:
    def __init__(self, cpm_name: str = 'Undefined', hourly_rate: float = 2.5, dateTime: str = 'ok') -> None:
        self.name = cpm_name
        self.rate = hourly_rate
        self.dateTime = dateTime

    def check_in(self, license_plate) -> None:
        with open(os.path.join(sys.path[0], 'carparklog.txt'), 'at') as parkFile:
            parkFile.writelines(f'{self.dateTime};cpm_name={self.name};license_plate={license_plate};action=check-in\n')

    def check_out(self, license_plate) -> None:
        text = f'{self.dateTime};cpm_name={self.name};license_plate={license_plate};action=check-out\n'
        with open(os.path.join(sys.path[0], 'carparklog.txt'), 'at') as parkFile:
            parkFile.writelines(text =+ self.get_total_car_fee(license_plate))

    def get_total_car_fee(self, lisence_plate) -> int or float:
        ...


if __name__ == "__main__":
    parkingMachine = CarParkingLogger(cpm_name='pepega')
    parkingMachine.check_in('sb-123-a')
    parkingMachine.check_in('sb-123-b')
    parkingMachine.check_in('sb-123-c')
    parkingMachine.check_out('sb-123-b')


# Datetime toevoegen aan checkin
# Maken manier laatste check-in te krijgen en daar de tijd uit halen
import sys
import os
from datetime import datetime
import re

class CarParkingLogger:
    def __init__(self, cpm_name: str = 'Undefined', hourly_rate: float = 2.5, dateTime: str = 'ok'):
        self.name = cpm_name
        self.rate = hourly_rate
        self.dateTime = dateTime
        self.dataStr = self.load_file()

    def load_file(self):
        return 'oksok'

    def check_in(self, license_plate: str):
        print(self.dataStr)

    def check_out(self, license_plate: str):
        ...

    def parking_fee(self, license_plate: str, dateTime: str = 'dateTime'):
        ...

if __name__ == "__main__":
    parkingMachine = CarParkingLogger(cpm_name='pepega')
    parkingMachine.check_in('sb-123-a')
    parkingMachine.check_in('sb-123-b')
    parkingMachine.check_in('sb-123-c')
    parkingMachine.check_out('sb-123-b')


#Load text file once load info into string = only checkins if not checkedout
#Load all checkins that have not been checkedout for specific self.name

#If checkin already exists in checkin list return false
    # date' 'time;cpm_name=...;license_plate=...;action=check-in

#If checkout license plate is in checkin list else return false
    # date' 'time;cpm_name=...;license_plate=...;action=check-in

#parking fee based on license plate in checkin data has own date time argument




'''
print(datetime.now())

class CarParkingLogger:
    def __init__(self, cpm_name: str = 'Undefined', hourly_rate: float = 2.5, dateTime: str = 'ok') -> None:
        self.name = cpm_name
        self.rate = hourly_rate
        self.dateTime = dateTime
        self.file = os.path.join(sys.path[0], 'carparklog.txt')

    def check_in(self, license_plate) -> None:
        text = f'{self.dateTime};cpm_name={self.name};license_plate={license_plate};action=check-in\n'
        open(self.file, 'a').writelines(text)

    def check_out(self, license_plate) -> None:
        license_plates = [re.split('=|;', i)[4] for i in open(self.file, 'r').readlines()]
        if license_plate in license_plates and license_plates.count(license_plate)%2 != 0:
            text = f'{self.dateTime};cpm_name={self.name};license_plate={license_plate};action=check-out;parking_fee='
            open(self.file, 'a').writelines(text + self.get_total_car_fee(license_plate) + '\n')
        else:
            return False

    def get_total_car_fee(self, lisence_plate) -> int or float:
        return 'bruh'


if __name__ == "__main__":
    parkingMachine = CarParkingLogger(cpm_name='pepega')
    parkingMachine.check_in('sb-123-a')
    parkingMachine.check_in('sb-123-b')
    parkingMachine.check_in('sb-123-c')
    parkingMachine.check_out('sb-123-b')

'''
# Datetime toevoegen aan checkin
# Maken manier laatste check-in te krijgen en daar de tijd uit halen
# If checkout car not in list return
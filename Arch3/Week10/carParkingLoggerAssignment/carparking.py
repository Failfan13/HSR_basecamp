import sys
import os
from datetime import datetime as dt
import re

class CarParkingLogger:
    def __init__(self, cpm_name: str = '', hourly_rate: float = 2.5, capacity = 10) -> None:
        self.name = cpm_name.lower().title()
        self.rate = hourly_rate
        self.capacity = capacity
        self.parked = 0
        self.dateTime = dt.now()
        self.dateTime.strftime('%d-%m-%Y %H:%M:%S')
        self.dataStr = ''
        self.load_file()

    def load_file(self) -> None:
        try:
            parkFile = open(os.path.join(sys.path[0], 'carparklog.txt'), 'rt').readlines()
        except (OSError, IOError):
            parkFile = []
        allParked = parkFile
        allParked.reverse()
        for line in allParked:
            if (re.split('=|;', line)[2] == self.name and 
                    re.split('=|;', line)[6] in ('check-in\n', 'check-in') and
                        ''.join(allParked).count(re.split('=|;', line)[4]) % 2 != 0 and
                            ''.join(self.dataStr).count(re.split('=|;', line)[4]) < 1):
                self.dataStr += (line if line.find('\n') > 0 else line +'\n')

    def check_in(self, license_plate: str) -> None:
        txt = f'{self.dateTime};cpm_name={self.name};license_plate={license_plate};action=check-in'
        (txt if len(self.dataStr) > 1 else '\r' + txt)
        if self.dataStr.count(license_plate) % 2 == 0 and self.parked <= self.capacity:
            with open(os.path.join(sys.path[0], 'carparklog.txt'), 'a') as parkFile:
                parkFile.write(txt)
            self.dataStr += txt
            self.parked += 1

    def check_out(self, license_plate: str) -> bool or None:
        txt = f'\r{self.dateTime};cpm_name={self.name};license_plate={license_plate};action=check-out'
        if self.dataStr.count(license_plate) % 2 != 0 and self.parked < self.capacity:
            txt += ';parking_fee=' + str(self.get_total_car_fee(license_plate))
            with open(os.path.join(sys.path[0], 'carparklog.txt'), 'a') as parkFile:
                parkFile.write(txt)
            self.dataStr += txt
            self.parked -= 1
            return True
            
    def get_total_car_fee(self, license_plate: str) -> float:
        for line in self.dataStr.split('\n'):
            if ((re.split('=|;', line)[4] if len(re.split('=|;', line)) > 1 else None) == license_plate):
                time = -(dt.strptime((line[:19] if line[:1] != '\r' else line[1:20]), '%d-%m-%Y %H:%M:%S') - 
                            dt.strptime(self.dateTime, '%d-%m-%Y %H:%M:%S')).total_seconds()//3600
        return self.rate * (24 if time > 24 else time if time > 1 else 1)

    def get_machine_fee_by_day(self, cpm_name: str = 'north', date: str = '09-02-2022') -> float:
        fees = 0.00
        with open(os.path.join(sys.path[0], 'carparklog.txt'), 'rt') as parkFile:
            for line in parkFile:
                if (re.split('=|;', line)[0][:10] == date and 
                        re.split('=|;', line)[2] == cpm_name.lower().title() and
                            len(re.split('=|;', line)) > 7):
                    fees += int(re.split('=|;', line)[8])
        return fees
            

if __name__ == "__main__":
    ...


# round returned total car fee to 2 decimals , # round return machine by day to 2 decimals
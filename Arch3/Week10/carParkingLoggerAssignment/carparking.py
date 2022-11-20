import sys
import os
from datetime import datetime as dt
import re

class CarParkingLogger:
    def __init__(self, cpm_name: str = '', hourly_rate: float = 2.5):
        self.name = cpm_name
        self.rate = hourly_rate
        self.dateTime = dt.now().strftime('%d-%m-%Y %H:%M:%S')
        self.dataStr = ''
        self.load_file()

    def load_file(self) -> None:
        parkFile = open(os.path.join(sys.path[0], 'carparklog.txt'), 'rt').readlines()
        allParked = parkFile
        allParked.reverse()
        for line in allParked:
            if (re.split('=|;', line)[2] == self.name and 
                    re.split('=|;', line)[6] in ('check-in\n', 'check-in') and
                        ''.join(allParked).count(re.split('=|;', line)[4]) % 2 != 0 and
                            ''.join(self.dataStr).count(re.split('=|;', line)[4]) < 1):
                self.dataStr += (line if line.find('\n') > 0 else line +'\n')

    def check_in(self, license_plate: str) -> None:
        txt = f'\r{self.dateTime};cpm_name={self.name};license_plate={license_plate};action=check-in'
        if self.dataStr.count(license_plate) % 2 == 0:
            with open(os.path.join(sys.path[0], 'carparklog.txt'), 'a') as parkFile:
                parkFile.write(txt)
            self.dataStr += txt

    def check_out(self, license_plate: str) -> None:
        txt = f'\r{self.dateTime};cpm_name={self.name};license_plate={license_plate};action=check-out'
        if self.dataStr.count(license_plate) % 2 != 0:
            txt += ';parking_fee=' + str(self.get_total_car_fee(license_plate))
            with open(os.path.join(sys.path[0], 'carparklog.txt'), 'a') as parkFile:
                parkFile.write(txt)
            self.dataStr += txt
            

    def get_total_car_fee(self, license_plate: str, dateTime: str = dt.now().strftime('%d-%m-%Y %H:%M:%S')) -> float:
        for line in self.dataStr.split('\n'):
            if ((re.split('=|;', line)[4] if len(re.split('=|;', line)) > 1 else None) == license_plate):
                time = -(dt.strptime(line[:19], '%d-%m-%Y %H:%M:%S') - 
                            dt.strptime(dateTime, '%d-%m-%Y %H:%M:%S')).total_seconds()//3600
        return self.rate * (time if time > 1 else 1)
            

if __name__ == "__main__":
    parkingMachine = CarParkingLogger(cpm_name='North')
    ...


# get_machine_fee_by_day method die 2 argumenten neemt, cpm_name : case insensitive(.title() is handig), search date form: DD-MM-YYYY,
# the returned fee should be rounded to 2 decimals

# round returned total car fee to 2 decimals
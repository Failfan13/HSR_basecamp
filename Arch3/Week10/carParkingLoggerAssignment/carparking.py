from datetime import datetime, timedelta


class CarParkingMachine:
    def __init__(self, capacity: int = 10, hourly_rate: float = 2.5, parked_cars: dict = {}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars

    def check_in(self, license_plate: str, check_in: str = datetime.now()) -> bool or None:
        if len(self.parked_cars) >= self.capacity or self.parked_cars.get(license_plate) != None:
            return False
        else:
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in.strftime("%d:%H:%M"))

    def get_parking_fee(self, license_plate: str) -> float:
        time = self.parked_cars.get(license_plate).checked_in.split(':')
        time = [int(time[0]), int(time[1]) if int(time[2]) < 30 else int(time[1])+1]
        time = [(datetime.now().hour - time[1]+1) 
                    if time[0] == datetime.now().day else 
                        (datetime.now().hour - time[1]+25)][0]
        return [self.hourly_rate if time < 1 else time*self.hourly_rate if time <= 24 else 24*self.hourly_rate][0]

    def check_out(self, license_plate: str) -> None:
        fee = self.get_parking_fee(license_plate)
        self.parked_cars.pop(license_plate)
        return fee

class ParkedCar:
    def __init__(self, license_plate: str, time) -> None:
        self.license_plate = license_plate
        self.checked_in = time



if __name__ == "__main__":
    cpm = CarParkingMachine() 

    while True:
        inp = input('''[I] Check-in car by license plate
[O] Check-out car by license plate
[Q] Quit program''').upper()

        if inp == 'I':
            inp = input().upper()
            if cpm.check_in(inp) is not False:
                print('License registered')
            else:
                print('Capacity reached!')
        elif inp == 'O':
            inp = input().upper()
            outp = cpm.check_out(inp)
            if outp is not None:
                print(f'Parking fee: {outp:.2f} EUR')
            else:
                print(f'License {inp} not found!')
        elif inp == 'Q':
            break

'''
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
        dateTime = self.dateTime.strftime('%d-%m-%Y %H:%M:%S')
        txt = f'{dateTime};cpm_name={self.name};license_plate={license_plate};action=check-in\n'
        #txt = txt if len(self.dataStr) < 1 else '\r' + txt
        if self.dataStr.count(license_plate) % 2 == 0 and self.parked < self.capacity:
            with open(os.path.join(sys.path[0], 'carparklog.txt'), 'a') as parkFile:
                parkFile.write(txt)
            self.dataStr += txt
            self.parked += 1

    def check_out(self, license_plate: str) -> bool or None:
        txt = f'{self.dateTime};cpm_name={self.name};license_plate={license_plate};action=check-out'
        if self.dataStr.count(license_plate) % 2 != 0:
            txt += ';parking_fee=' + str(self.get_total_car_fee(license_plate)) + '\n'
            with open(os.path.join(sys.path[0], 'carparklog.txt'), 'a') as parkFile:
                parkFile.write(txt)
            self.dataStr += txt
            self.parked -= 1
            return True
            
    def get_total_car_fee(self, license_plate: str) -> float:
        for line in re.split('\n|\r', self.dataStr):
            if (re.split('=|;', line)[4] if len(re.split('=|;', line)) > 1 else None) == license_plate:
                time = -((dt.strptime((line[:19] if line[:1] != '\r' else line[1:20]), '%d-%m-%Y %H:%M:%S')) -
                        dt.now()).total_seconds() // 3600
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
            

def main():
    cpl = CarParkingMachine(id="North",capacity=2, hourly_rate=4.0)
    while True:
        inp = input(''[I] Check-in car by license plate
[O] Check-out car by license plate
[Q] Quit program'').lower()
        if inp == 'i':
            inp = input('numberplate').upper()
            cpl.check_in(inp)
        elif inp == 'o':
            inp = input('numberplate').upper()
            cpl.check_out(inp)
        elif inp == 'q':
            break

if __name__ == "__main__":
    main()
'''
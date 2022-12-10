from datetime import datetime as dt, timedelta
import os
import sys
import json

class CarParkingMachine:
    def __init__(self, id='North', capacity: int = 10, hourly_rate: float = 2.5):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.logger = CarParkingLogger(id)
        self.parked_cars = self.logger.check_state()

    def check_in(self, license_plate: str, check_in: str = dt.now()) -> None:
        if not valueInAnyJson(license_plate) and len(self.parked_cars) < self.capacity:
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in.strftime('%d-%m-%Y %H:%M:%S'))
            self.logger.checker(self.parked_cars[license_plate], self.parked_cars)
            return True
        return False

    def get_parking_fee(self, license_plate: str) -> float:
        if license_plate in self.parked_cars.keys():
            time = -(dt.strptime(self.parked_cars.get(license_plate).checked_in, '%d-%m-%Y %H:%M:%S') -
                        dt.now()).total_seconds() //3600
            return self.hourly_rate * (24 if time > 24 else time if time > 1 else 1)
        return False

    def check_out(self, license_plate: str) -> bool or None:
        if license_plate in self.parked_cars.keys():
            fee = self.get_parking_fee(license_plate)
            car = self.parked_cars[license_plate]
            self.parked_cars.pop(license_plate)
            self.logger.checker(car, self.parked_cars, check='out', fee=fee)
            return fee
        return False

class ParkedCar:
    def __init__(self, license_plate: str, time) -> None:
        self.license_plate = license_plate
        self.checked_in = time

class CarParkingLogger:
    def __init__ (self, cpm_name):
        self.cpm_name = cpm_name
        self.cpm_id = f'{self.cpm_name}_state'

    def checker(self, parkedCar:object, parked_cars:list, check:str='in', fee:float=0):
        line = f'{parkedCar.checked_in};cpm_name={self.cpm_name};license_plate={parkedCar.license_plate};action=check'
        with open(os.path.join(sys.path[0], 'carparklog.txt'), 'a') as f:
            f.write(line + f'-out;parking_fee={fee}\n' if not check == 'in' else line + f'-in\n')
            f.close()
        try:
            with open(os.path.join(sys.path[0], self.cpm_id + '.json'), mode='w') as jsonFile:
                json.dump([{'license_plate': v.license_plate, 'check_in': v.checked_in} 
                    for k,v in parked_cars.items()], jsonFile, indent = 4)
        except ValueError:
            pass

    def check_state(self) -> dict:
        checkedIn = {}
        try:
            with open(os.path.join(sys.path[0], self.cpm_id + '.json'), mode='r') as jsonFile:
                try:
                    oldData = json.load(jsonFile)
                    checkedIn = {d.get('license_plate'):ParkedCar(d.get('license_plate'), d.get('check_in')) for d in oldData}
                except json.decoder.JSONDecodeError:
                    pass
        except FileNotFoundError:
            pass
        return checkedIn

    def get_machine_fee_by_day(self, cpm_name:str, license_plate:str, ) -> None:
        calcFee('machine', cpm_name, license_plate)

    def get_total_car_fee(self, license_plate) -> None:
        calcFee('car', license_plate)


def calcFee(type:str, license_plate:str, cpm_name:str='') -> float:
    fee = 0
    line = float(line.split(';')[4][line.split(';')[4].index('=') + 1:])
    with open(os.path.join(sys.path[0], 'carparklog.txt'), 'r') as fileText:
        if not 0 >= type.find('total') or type.find('car'):
            for line in fileText:
                if (line.split(';')[1] == f'cpm_name={cpm_name}' and len(line.split(';')) > 4):
                    fee += line
        else:
            for line in fileText:
                if line.find(license_plate) >= 0 and len(line.split(';')) > 4:
                    fee += line
    return fee


def valueInAnyJson(value:str) -> bool:
    try:
        for file in os.listdir(sys.path[0]):
                if file.endswith('.json'):
                    with open(os.path.join(sys.path[0], file), mode='r') as f:
                        try:
                            data = json.load(f)
                            if value in tuple([v for d in data for v in d.values()]):
                                return True
                        except json.decoder.JSONDecodeError:
                            pass
    except FileNotFoundError:
        pass
    return False


if __name__ == "__main__":
    cpm = CarParkingMachine()
    while True:
        cpm = CarParkingMachine()
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

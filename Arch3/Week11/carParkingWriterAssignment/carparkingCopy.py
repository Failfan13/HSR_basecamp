from datetime import datetime as dt, timedelta as td
import os
import sys
import json

class CarParkingMachine:
    def __init__(self, id='North', capacity: int = 10, hourly_rate: float = 2.5):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.logger = CarParkingLogger(cpm_name=id, cpm_id=f'parking-machine-{id.lower()}') # 1e object = parking-machine-north 2e = parking-machine-south
        self.parked_cars = self.logger.check_state()

    def check_in(self, license_plate: str, check_in: str = dt.now()) -> None:
        if not valueInAnyJson(license_plate):
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in.strftime('%d-%m-%Y %H:%M:%S'))
            self.logger.check_in(self.parked_cars[license_plate], self.parked_cars)
        else:
            return False

    def get_parking_fee(self, license_plate: str) -> float:
        if license_plate in self.parked_cars.keys():
            time = - (dt.strptime(self.parked_cars.get(license_plate).checked_in, '%d-%m-%Y %H:%M:%S') -
                        dt.now()).total_seconds() //3600
            return self.hourly_rate * (24 if time > 24 else time if time > 1 else 1)

    def check_out(self, license_plate: str) -> bool or None:
        if license_plate in self.parked_cars.keys():
            fee = self.get_parking_fee(license_plate)
            self.logger.check_out(self.parked_cars[license_plate], fee, self.parked_cars)
            self.parked_cars.pop(license_plate)
            return fee
        else:
            return False

class ParkedCar:
    def __init__(self, license_plate: str, time) -> None:
        self.license_plate = license_plate
        self.checked_in = time

class CarParkingLogger:
    def __init__ (self, cpm_name, cpm_id):
        self.cpm_name = cpm_name
        self.cpm_id = cpm_id
        self.readFile = open('carparklog.txt', 'r')
        self.writeFile = open('carparklog.txt', 'a')

    def check_in(self, parkedCar:object, parked_cars:list):
        self.writeFile.write(f'{parkedCar.checked_in};cpm_name={self.cpm_name};license_plate={parkedCar.license_plate};action=check-in\n')
        try:
            with open(os.path.join(sys.path[0], self.cpm_id + '.json'), mode='w') as jsonFile:
                json.dump([{'license_plate': v.license_plate, 'check_in': v.checked_in} for k,v in parked_cars.items()], jsonFile, indent = 4)
        except ValueError:
            print('invalid')

    def check_out(self, parkedCar:object, fee:float, parked_cars:list):
        self.writeFile.write(
            f'{parkedCar.checked_in};cpm_name={self.cpm_name};license_plate={parkedCar.license_plate};action=check-out;parking_fee={fee}\n')
        try:
            with open(os.path.join(sys.path[0], self.cpm_id + '.json'), mode='w') as jsonFile:
                json.dump([{'license_plate': v.license_plate, 'check_in': v.checked_in} for k,v in parked_cars.items()], jsonFile, indent = 4)
        except ValueError:
            print('invalid')

    def check_state(self) -> dict:
        # checkedIn = {}
        # with self.readFile as fileText:
        #     text = list(fileText)
        #     text.reverse()
        #     for line in text:
        #         plate = line.split(';')[2][line.split(';')[2].index('=') + 1:]
        #         if ''.join(text).count(plate) % 2 != 0:
        #             if plate not in checkedIn.keys():
        #                 checkedIn[plate] = ParkedCar(plate, line[:19])
        # return checkedIn
        checkedIn = {}
        try:
            with open(os.path.join(sys.path[0], self.cpm_id + '.json'), mode='r') as jsonFile:
                try:
                    oldData = json.load(jsonFile)
                    checkedIn = {d.get('license_plate'):ParkedCar(d.get('license_plate'), d.get('check_in')) for d in oldData}
                except json.decoder.JSONDecodeError:
                    pass
        except FileNotFoundError:
            print('invalid')
        return checkedIn # 1e object = {} 2e = {} klopt

    def get_machine_fee_by_day(self, *args) -> float:
        fee = 0
        with self.readFile as fileText:
            for line in fileText:
                if (line.split(';')[1] == f'cpm_name={args[0]}' and len(line.split(';')) > 4):
                    fee += float(line.split(';')[4][line.split(';')[4].index('=') + 1:])
        return fee

    def get_machine_fee_by_day(self, *args) -> float:
        fee = 0
        with self.readFile as fileText:
            for line in fileText:
                if (line.split(';')[1] == f'cpm_name={args[0]}' and len(line.split(';')) > 4):
                    fee += float(line.split(';')[4][line.split(';')[4].index('=') + 1:])
        return fee

    def get_total_car_fee(self, license_plate):
        fee = 0
        with self.readFile as fileText:
            for line in fileText:
                if line.find(license_plate) >= 0 and len(line.split(';')) > 4:
                    fee += float(line.split(';')[4][line.split(';')[4].index('=') + 1:])
        return fee


def valueInAnyJson(value:str):
    for file in os.listdir(sys.path[0]):
        if file.endswith('.json'):
            with open(os.path.join(sys.path[0], file), mode='r') as f:
                try:
                    data = json.load(f)
                    if value in tuple([v for d in data for v in d.values()]):
                        return True
                except json.decoder.JSONDecodeError:
                    pass
    return False


if __name__ == "__main__":
    cpm = CarParkingMachine()
    cpm.check_in('45-DEF-6')
    cpm.check_in('45-DEF-5')
    cpm2 = CarParkingMachine(id='South')
    cpm2.check_in('45-DEF-4')

#     while True:
#         inp = input('''[I] Check-in car by license plate
# [O] Check-out car by license plate
# [Q] Quit program''').upper()

#         if inp == 'I':
#             inp = input().upper()
#             if cpm.check_in(inp) is not False:
#                 print('License registered')
#             else:
#                 print('Capacity reached!')
#         elif inp == 'O':
#             inp = input().upper()
#             outp = cpm.check_out(inp)
#             if outp is not None:
#                 print(f'Parking fee: {outp:.2f} EUR')
#             else:
#                 print(f'License {inp} not found!')
#         elif inp == 'Q':
#             break

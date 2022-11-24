from datetime import datetime as dt, timedelta

class CarParkingMachine:
    def __init__(self, id='North', capacity: int = 10, hourly_rate: float = 2.5, parked_cars: dict = {}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars
        self.logger = CarParkingLogger(cpm_name=id)
        self.parked_cars.update(self.logger.check_state())


    def check_in(self, license_plate: str, check_in = dt.now()) -> None:
        if (license_plate not in self.parked_cars.keys() and len(self.parked_cars) < self.capacity):
            if self.parked_cars.get(license_plate) != bool or None:
                self.parked_cars[license_plate] = ParkedCar(license_plate, check_in.replace(microsecond=0))
                self.logger.check_in(self.parked_cars[license_plate])
        else:
            return False


    def get_parking_fee(self, license_plate: str) -> float:
        if license_plate in self.parked_cars.keys():
            time = - (self.parked_cars.get(license_plate).check_in -
                        dt.now()).total_seconds() //3600
            return self.hourly_rate * (24 if time > 24 else time if time > 1 else 1)


    def check_out(self, license_plate: str) -> bool or None:
        if license_plate in self.parked_cars.keys():
            fee = self.get_parking_fee(license_plate)
            self.logger.check_out(self.parked_cars[license_plate], fee)
            self.parked_cars.pop(license_plate)
            return fee
        else:
            return False

class ParkedCar:
    def __init__(self, license_plate: str, time) -> None:
        self.license_plate = license_plate
        self.check_in = dt.strptime(str(time), "%Y-%m-%d %H:%M:%S")



class CarParkingLogger:
    def __init__ (self, cpm_name):
        self.cpm_name = cpm_name

    def read_file(self):
        with open('carparklog.txt', 'r') as f:
            return f.readlines()

    def write_file(self, inp):
        with open('carparklog.txt', 'a') as w:
            return w.write(inp)

    def check_in(self, *args):
        self.write_file(f'{args[0].check_in};cpm_name={self.cpm_name};license_plate={args[0].license_plate};action=check-in\n')


    def check_out(self, *args):
        self.write_file(f'{args[0].check_in};cpm_name={self.cpm_name};license_plate={args[0].license_plate};action=check-out;parking_fee={args[1]}\n')

    def check_state(self) -> dict:
        checkedIn = {}
        text = self.read_file()
        text.reverse()
        for line in text:
            plate = line.split(';')[2][line.split(';')[2].index('=') + 1:]
            if ''.join(text).count(plate) % 2 != 0:
                if plate not in checkedIn.keys():
                    checkedIn[plate] = ParkedCar(plate, str(line[:19]))
        return checkedIn

    def get_machine_fee_by_day(self, *args) -> float:
        fee = 0
        for line in self.read_file():
            if (line.split(';')[1] == f'cpm_name={args[0]}' and len(line.split(';')) > 4):
                fee += float(line.split(';')[4][line.split(';')[4].index('=') + 1:])
        return round(fee, 2)
    
    
    def get_total_car_fee(self, license_plate):
        fee = 0
        for line in self.read_file():
            if line.find(license_plate) >= 0 and len(line.split(';')) > 4 and line.find(self.cpm_name) >= 0:
                fee += float(line.split(';')[4][line.split(';')[4].index('=') + 1:])
        return round(fee, 2)


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
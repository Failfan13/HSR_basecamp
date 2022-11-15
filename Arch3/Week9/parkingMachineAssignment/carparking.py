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
from datetime import datetime, timedelta


class CarParkingMachine:
    def __init__(self, capacity: int = 10, hourly_rate: float = 2.5, parked_cars: dict = {}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars

    def check_in(self, lP: str, time: str = datetime.now().strftime("%d:%H:%M")) -> bool or None:
        if len(self.parked_cars) >= self.capacity or self.parked_cars.get(lP) != None:
            return False
        else:
            self.parked_cars[lP] = ParkedCar(lP, time)

    def get_parking_fee(self, lP: str) -> float:
        time = self.parked_cars.get(lP).checked_in.split(':')
        time = [int(time[0]), int(time[1]) if int(time[2]) < 30 else int(time[1])+1]
        time = [(datetime.now().hour - time[1]+1) 
                    if time[0] == datetime.now().day else 
                        (datetime.now().hour - time[1]+25)][0]
        self.parked_cars.pop(lP)
        return [self.hourly_rate if time < 1 else time*self.hourly_rate if time <= 24 else 24*self.hourly_rate][0]

class ParkedCar:
    def __init__(self, lP: str, time) -> None:
        self.license_plate = lP
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
            outp = cpm.get_parking_fee(inp)
            if outp is not None:
                print(f'Parking fee: {outp:.2f} EUR')
            else:
                print(f'License {inp} not found!')
        elif inp == 'Q':
            break
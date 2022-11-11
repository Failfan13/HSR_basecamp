from datetime import datetime, timedelta


class CarParkingMachine:
    def __init__(self, capacity: int = 10, hourly_rate: float = 2.5, parked_cars: dict = {}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars

    def check_in(self, lP: str, time: str = datetime.now().strftime("%H:%M")) -> bool or None:
        if len(self.parked_cars) > self.capacity:
            return False
        else:
            self.parked_cars[lP] = ParkedCar(lP, time)

    def get_parking_fee(self, lP: str) -> float:
        time = self.parked_cars.get(lP).checked_in.split(':')
        time = [int(time[0]) if int(time[1]) < 30 else int(time[0])+1][0]
        time = (time - datetime.now().hour)
        return [1 if time == 0 else time][0] * self.hourly_rate


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

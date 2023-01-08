import sys
import os
import sqlite3 as sql
from datetime import datetime as dt, timedelta

class CarParkingMachine:
    def __init__(self, id='North', capacity: int = 10, hourly_rate: float = 2.5) -> None:
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.cpm_name = id
        self.db_con = sql.connect(os.path.join(sys.path[0], 'carparkingmachine.db'))
        self.db_con.execute(
            """CREATE TABLE IF NOT EXISTS parkings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_parking_machine TEXT NOT NULL,
                license_plate TEXT NOT NULL,
                check_in TEXT NOT NULL,
                check_out TEXT DEFAULT NULL,
                parking_fee NUMERIC DEFAULT 0 
            );"""
        )
        self.parked_cars = restoreState(self.db_con, self.cpm_name)

    # Checkin / Insert new car
    def check_in(self, license_plate: str, check_in: str = dt.now()) -> None:
        if len(self.parked_cars) < self.capacity and self.find_last_checkin(license_plate) == True:
            parkedInsert = self.insert(ParkedCar(license_plate, check_in.strftime('%d-%m-%Y %H:%M:%S')))
            self.parked_cars[license_plate] = parkedInsert
            return True
        return False

    # Checkout / Update existing car
    def check_out(self, license_plate: str) -> bool or None:
        if license_plate in self.parked_cars.keys():
            parkedObj = self.parked_cars[license_plate]
            parkedObj.check_out = dt.now().strftime('%d-%m-%Y %H:%M:%S')
            fee = self.get_parking_fee(license_plate)
            parkedObj.parking_fee = fee
            self.update(parkedObj)
            self.parked_cars.pop(license_plate)
            return fee

    # Calculate parking fee
    def get_parking_fee(self, license_plate: str) -> float:
        if license_plate in self.parked_cars.keys():
            time = -(dt.strptime(self.parked_cars.get(license_plate).check_in, '%d-%m-%Y %H:%M:%S') -
                        dt.now()).total_seconds() //3600
            return self.hourly_rate * (24 if time > 24 else time if time > 1 else 1)
        return False

    # Find car by calling id
    def find_by_id(self, id) -> object:
        parkedCar = self.db_con.execute(
            f'''SELECT license_plate, check_in
                FROM parkings
                WHERE id = "{id}"'''
        )
        return ParkedCar(*parkedCar.fetchone())

    # Find last not checked out car
    def find_last_checkin(self, license_plate:str) -> object or bool:
        lastInstance = self.db_con.execute(
            f'''SELECT license_plate, check_in
                FROM parkings
                WHERE license_plate = "{license_plate}"
                    AND check_out IS NULL'''
        ).fetchone()
        if not lastInstance == None:
            return ParkedCar(*lastInstance)
        return True
    
    # Insert new parked car into database
    def insert(self, parked_car:object) -> object:
        self.db_con.execute(
            '''INSERT INTO parkings ('car_parking_machine', 'license_plate', 
                    'check_in')
                VALUES {}'''.format((self.cpm_name, parked_car.license_plate, 
                    parked_car.check_in))
        )
        self.db_con.commit()
        insertObj =  self.db_con.execute(
            '''SELECT id, license_plate, check_in
                FROM parkings
                WHERE car_parking_machine = "{}"
                    AND license_plate = "{}"
                    AND check_in = "{}"
                    '''.format(self.cpm_name, parked_car.license_plate, 
                    parked_car.check_in)
        )
        fetchObj = insertObj.fetchone()
        parkedCar = ParkedCar(*fetchObj[1:])
        parkedCar.id = fetchObj[0]
        return parkedCar

    # update existing ID in database
    def update(self, parked_car:object) -> None:
        self.db_con.execute(
                '''UPDATE parkings
                    SET check_out = "{}",
                        parking_fee = "{}"
                    WHERE id = {}
                    '''.format(parked_car.check_out, parked_car.parking_fee, parked_car.id)
            )
        self.db_con.commit()

#Create ParkedCar Objects
class ParkedCar:
    def __init__(self, license_plate:str, time_in:str, time_out:str='ok', 
            id:int=0, parking_fee:float=0) -> None:
        self.id = id
        self.license_plate = license_plate
        self.check_in = time_in
        self.check_out = time_out
        self.parking_fee = parking_fee

# load non checkout instances from cpm.db -> file.db to cpm.parked_cars -> self of cpm
def restoreState(dataBase:sql.Connection, cpm_id) -> dict:
    parked = dataBase.execute(
        f'''SELECT license_plate, check_in, check_out, id
            FROM parkings
            WHERE car_parking_machine = "{cpm_id}" AND check_out IS NULL'''
    ).fetchall()
    return {t[0]: ParkedCar(*t) for t in parked}

if __name__ == "__main__":
    cpm = CarParkingMachine(hourly_rate=4.0)
    cpm.check_in('BB-494-H')
#     cpm = CarParkingMachine()
#     while True:
#         inp = input('''[I] Check-in car by license plate
# [O] Check-out car by license plate
# [Q] Quit program''').upper()
#         if inp == 'I':
#             if cpm.check_in(input().upper()) is not False:
#                 print('License registered!')
#             elif cpm.capacity >= len(cpm.parked_cars):
#                 print('Capacity reached!')
#             else:
#                 print('Already Parked!')
#         elif inp == 'O':
#             outp = cpm.check_out(input().upper())
#             if outp is not None:
#                 print(f'Parking fee: {outp:.2f} EUR')
#             else:
#                 print(f'License {inp} not found!')
#         elif inp == 'Q':
#             break

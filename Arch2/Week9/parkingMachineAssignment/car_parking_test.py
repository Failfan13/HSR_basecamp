from file import *
from datetime import datetime, timedelta

'''
PyTest template file. Use asserts to test your class code.
Don't forget to put this file in the same location as your carparkingmachine.py

Hint: use the datetime module (datetime and timedelta objects) to test with a check-in time in the past.
Example: my_datetime = datetime.now() - timedelta(hours=2, minutes=10)
This statement creates a datetime object 2 hours and 10 minutes in the past.
'''
# object
cmp = CarParkingMachine(capacity=2)

# Test check_in & parked_cars
def test_check_in_capacity():
    cmp.check_in('BB-49-JF')
    cmp.check_in('21-TIV-8')
    assert len(cmp.parked_cars) == 2
    assert cmp.check_in('22-TId-9') == False
    cmp.parked_cars = {}


# Test parking fee
def test_parking_fee():
    cmp.check_in('GH-56-31', (datetime.now() - timedelta(hours=5, minutes=00)).strftime("%d:%H:%M"))
    cmp.check_in('jkc-4-gi', (datetime.now() - timedelta(hours=30, minutes=40)).strftime("%d:%H:%M"))
    assert cmp.get_parking_fee('GH-56-31') == 15.0
    assert cmp.get_parking_fee('jkc-4-gi') == 60.0
    cmp.parked_cars = {}

# Test check-out
def test_check_out():
    cmp.check_in('14-HGD-6', (datetime.now() - timedelta(hours=5, minutes=00)).strftime("%d:%H:%M"))
    cmp.get_parking_fee('14-HGD-6')
    assert cmp.parked_cars.get('14-HGD-6') == None 
    cmp.parked_cars = {}

# Test al bestaand
def test_predefined():
    cmp.check_in('BB-49-JF')
    assert cmp.check_in('BB-49-JF') == False
    cmp.parked_cars = {}
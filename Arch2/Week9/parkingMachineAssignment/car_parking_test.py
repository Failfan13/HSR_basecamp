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

# Test parking fee
def test_parking_fee():
    cmp.check_in('GH-56-31', (datetime.now() - timedelta(hours=2, minutes=10)).strftime("%H:%M"))
    print(cmp.get_parking_fee('GH-56-31'))
    cmp.check_in('jkc-4-gi', (datetime.now() + timedelta(hours=26, minutes=10)).strftime("%H:%M"))
    print(cmp.get_parking_fee('jkc-4-gi'))
    # check-in cars at multiple timestamps and check that the calculated fee is correct
    # check that the maximum fee is not exceeded when parking for more than 24 hours
    ...
# Test check-out
def test_check_out():
    # check that checked-out cars are removed from the parked_cars dict
    # check that a car checked-in and checked-out directly after has an 1 hour fee
    ...

# Test al bestaand
def test_predefined():
    ...

test_parking_fee()
from carparking import *
from datetime import datetime, timedelta

cmp = CarParkingMachine(capacity=2)

# object
def test_carparkingmachine():
    assert cmp != None

# Test check_in & parked_cars
def test_check_in_capacity():
    cmp.check_in('BB-49-JF', (datetime.now() - timedelta(hours=5, minutes=00)))
    cmp.check_in('21-TIV-8', (datetime.now() - timedelta(hours=30, minutes=40)))
    assert len(cmp.parked_cars) == 2
    assert cmp.check_in('22-TId-9') == False

# Test parking fee
def test_parking_fee():
    assert cmp.get_parking_fee('BB-49-JF') == 12.5
    assert cmp.get_parking_fee('21-TIV-8') == 60.0

# Test check-out
def test_check_out():
    assert cmp.check_out('BB-49-JF') is not False

# Test al bestaand
def test_predefined():
    cmp.check_in('BB-49-JF')
    assert cmp.check_in('BB-49-JF') == False
    cmp.check_out('BB-49-JF')
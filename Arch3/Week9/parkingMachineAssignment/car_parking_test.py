from carparking import *
from datetime import datetime, timedelta

cmp = CarParkingMachine(capacity=2)

# object
def test_carparkingmachine():
    assert cmp != None

# Test check_in & parked_cars
def test_check_in_capacity():
    cmp.check_in('BB-49-JF')
    cmp.check_in('21-TIV-8')
    assert len(cmp.parked_cars) == 2
    assert cmp.check_in('22-TId-9') == False
    cmp.check_out('BB-49-JF')
    cmp.check_out('21-TIV-8')

# Test parking fee
def test_parking_fee():
    cmp.check_in('GH-56-31', (datetime.now() - timedelta(hours=5, minutes=00)))
    cmp.check_in('jkc-4-gi', (datetime.now() - timedelta(hours=30, minutes=40)))
    assert cmp.get_parking_fee('GH-56-31') == 15.0
    assert cmp.get_parking_fee('jkc-4-gi') == 60.0
    cmp.check_out('GH-56-31')
    cmp.check_out('jkc-4-gi')

# Test check-out
def test_check_out():
    cmp.check_in('14-HGD-6', (datetime.now() - timedelta(hours=5, minutes=00)))
    cmp.get_parking_fee('14-HGD-6')
    assert cmp.check_out('14-HGD-6') == 15.0

# Test al bestaand
def test_predefined():
    cmp.check_in('BB-49-JF')
    assert cmp.check_in('BB-49-JF') == False
    cmp.check_out('BB-49-JF')
from carparking import *
from datetime import datetime as dt, timedelta

cmp = CarParkingLogger(cpm_name='North', hourly_rate=2, capacity=2)

# object
def test_carparkingmachine() -> None:
    assert cmp != None

# Test check_in & parked_cars
def test_check_in_capacity():
    cmp.check_in('SH-123-A')
    cmp.dateTime = dt.now() + timedelta(hours=4)
    cmp.check_in('SH-123-B')
    cmp.check_in('SH-123-C')
    assert cmp.parked == 2

# Test parking fee
def test_parking_fee() -> None:
    assert cmp.get_total_car_fee('SH-123-A') == 2
    assert cmp.get_total_car_fee('SH-123-B') == 8

# Test check-out
def test_check_out() -> None:
    assert cmp.check_out('SH-123-A') == True
    assert cmp.check_out('SH-123-B') == True
    assert cmp.check_out('SH-123-C') == None|False

# Test al bestaand
def test_predefined() -> None:
    cmp.check_in('SH-123-A')
    cmp.check_in('SH-123-A')
    assert cmp.parked == 1
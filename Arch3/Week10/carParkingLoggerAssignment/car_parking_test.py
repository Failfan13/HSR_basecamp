from carparking import *
from datetime import datetime, timedelta

# object
def test_carparkingmachine():
    cmp = CarParkingMachine(capacity=2)
    assert cmp != None

# Test check_in & parked_cars
def test_check_in_capacity():
    cmp = CarParkingMachine(capacity=2)
    cmp.check_in('BB-49-JF')
    cmp.check_in('21-TIV-8')
    assert False == cmp.check_in('22-TId-9')
    assert 2 == len(cmp.parked_cars)

# Test parking fee
def test_parking_fee():
    cmp = CarParkingMachine(id='South')
    cmp.check_in(license_plate='AAA', check_in=dt.now() - timedelta(hours=2, minutes=10))
    cmp.check_in(license_plate='BBB', check_in=dt.now() - timedelta(hours=24))
    cmp.check_in(license_plate='CCC', check_in=dt.now() - timedelta(hours=30))
    assert None != cmp.get_parking_fee("AAA")

# Test check-out
def test_check_out():
    cmp = CarParkingMachine()
    cmp.check_in('BB-49-JF')
    assert False != cmp.check_out('BB-49-JF')

# Test al bestaand
def test_predefined():
    cmp = CarParkingMachine()
    cmp.check_in('BB-49-JF')
    assert False == cmp.check_in('BB-49-JF')
    cmp.check_out('BB-49-JF')

def test_get_machine_fee_by_day():
    cpm = CarParkingMachine(id='0123796423643512323', hourly_rate=1.55)
    
    cpm.check_in(license_plate='KKK', check_in=dt.now() - timedelta(hours=30))
    cpm.check_out(license_plate='KKK')
    cpm.check_in(license_plate='KKK')
    cpm.check_out(license_plate='KKK')
    cpm.check_in(license_plate='JJJ')
    cpm.check_out(license_plate='JJJ')
    cpm.check_in(license_plate='LLL')
    cpm.check_out(license_plate='LLL')
    cpm.check_in(license_plate='MMM')

    cpm.logger.get_machine_fee_by_day('0123796423643512323', dt.now().strftime('%d-%m-%Y'))
test_get_machine_fee_by_day()
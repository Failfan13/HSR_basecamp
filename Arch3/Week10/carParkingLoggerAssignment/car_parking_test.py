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

# Test alle kosten per datum berekenen
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

    assert 41.85 == cpm.logger.get_machine_fee_by_day('0123796423643512323', dt.now().strftime('%d-%m-%Y'))

# Test kosten van bepaalde nummerplaat berekenen
def test_get_total_car_fee():
    cpm_1 = CarParkingMachine(id='cpm_1', hourly_rate=4)
    cpm_1.check_in('123-ab-4', check_in=dt.now() - timedelta(hours=30))
    cpm_1.check_out('123-ab-4')
    cpm_1.check_in('123-ab-4')
    cpm_1.check_out('123-ab-4')

    cpm_2 = CarParkingMachine(id='cpm_2', hourly_rate=0.5)
    cpm_2.check_in('123-ab-4')
    cpm_2.check_out('123-ab-4')

    cpm_3 = CarParkingMachine(id='cpm_3', hourly_rate=6.25)
    cpm_3.check_in('123-ab-4')
    cpm_3.check_out('123-ab-4')
    cpm_3.check_in('123-ab-4')
    
    assert 100 == cpm_1.logger.get_total_car_fee('123-ab-4')
    assert 0.5 == cpm_2.logger.get_total_car_fee('123-ab-4')
    assert 6.25 == cpm_3.logger.get_total_car_fee('123-ab-4')


def test_restore_state():
        check_in = datetime.now() - timedelta(minutes=10)
    
        cpm_north = CarParkingMachine(id='cpm_1')
        cpm_north.check_in(license_plate='RRR', check_in=check_in)
        cpm_north.check_in(license_plate='TTT', check_in=check_in)
        cpm_north.check_out(license_plate='TTT')

        cpm_north = CarParkingMachine(id='cpm_1')
        assert True == ('RRR' in cpm_north.parked_cars)
        assert True == check_in.replace(microsecond=0) == cpm_north.parked_cars['RRR'].check_in

test_restore_state()
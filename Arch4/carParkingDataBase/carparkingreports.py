import sys
import os
import csv
import sqlite3 as sql


def allParkedReport(in_date:str='', out_date:list='', machine:str='', license:str=''):
    allParked = dictAllParked(in_date, out_date, machine, license)
    csvListDict = []
    tempDict = {}
    headerList = []
    fileName = ''
    for car in allParked:
        obj = carParkedObj(car)
        if not machine == '':   
            headerList = ["license_plate","check-in",
                "check-out","parking_fee"]       
            fileName = 'parkedcars_{}_from_{}_to_{}'.format(machine, in_date, out_date)
            obj.pop('cpm_name')
            csvListDict.append({headerList[i]:(v if not v is None else 'None') for i,v in enumerate(obj.values())})
        elif license == '':
            headerList = ['car_parking_machine', 'total_parking_fee']
            fileName = 'totalfee_from_{}_to_{}'.format(in_date, out_date)
            if not obj.get('cpm_name').lower() in tempDict.values():
                tempDict['car_parking_machine'] = obj.get('cpm_name').lower()
                tempDict['total_parking_fee'] = 0
            tempDict['total_parking_fee'] += obj.get('fee')
        else:
            headerList = ["car_parking_machine","check_in",
                "check_out","parking_fee"]       
            fileName = 'complete_parkings_{}'.format(license)
            obj.pop('license')
            csvListDict.append({headerList[i]:(v if not v is None else 'None') for i,v in enumerate(obj.values())})
    if not tempDict == {}:
        csvListDict.append(tempDict)
    if not csvListDict == []:
        writeToCSV(csvListDict, headerList, fileName)
    exit()
        
def dictAllParked(in_date:str, out_date:str, machine, license) -> list:
    con = sql.connect(os.path.join(sys.path[0], 'carparkingmachine.db'))
    queryVals = [in_date, out_date]
    query = '''SELECT car_parking_machine, license_plate, check_in, check_out, parking_fee
            FROM parkings
            WHERE check_in BETWEEN ? AND ?'''
    if not machine == "":
        query += " AND car_parking_machine = ?"
        queryVals.append(machine)
    if not license == "":
        query = query[:-24] + " license_plate = ?"
        queryVals = [license]
    return con.execute(query,queryVals).fetchall()


def carParkedObj(parked:tuple):
    keys = ['cpm_name', 'license', 'check_in', 'check_out', 'fee']
    return {keys[i]:v for i,v in enumerate(parked)}


def writeToCSV(listDict:list, fieldNames:list, fileName:str):
    with open(os.path.join(sys.path[0], '{}.csv'.format(fileName)), mode='w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=';')
        writer.writeheader()
        for dict in listDict:
            writer.writerow(dict)


def menuStructure():
    """[P] Report all parked cars during a parking period for a specific parking machine
[F] Report total collected parking fee during a parking period for all parking machines
[C] Report all complete parkings over all parking machines for a specific car
[Q] Quit program"""


def main():
    while True:
        inp = input(menuStructure.__doc__).upper()
        if inp == 'P':
            inp = input('cpm, start date, end date').split(',')
            allParkedReport(inp[1], inp[2], machine=inp[0])
        elif inp == 'F':
            inp = input('start date, end date').split(',')
            allParkedReport(inp[0], inp[1])
        elif inp == 'C':
            inp = input('input a license').upper()
            allParkedReport(license=inp)
        elif inp == 'Q':
            break
        else:
            print('invalid')

if __name__ == "__main__":
    main()
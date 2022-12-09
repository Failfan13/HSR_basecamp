import sys
import os
import csv


def allParkedReport(in_date:str, out_date:list, machine:str=''):
    csvListDict = []
    headerList = []
    listCheckout = dictAllParked(in_date, out_date)
    if not machine == '':
        headerList = ["license_plate","check-in","check-out","parking_fee"] 
        for dict in listCheckout:
            if dict.get('cpm_name') == machine.lower().title():
                csvListDict.append({'license_plate':dict.get('license_plate'), 'check-in':dict.get('date-in'), 
                    'check-out':dict.get('date'), 'parking_fee':dict.get('parking_fee').strip('\n').strip('\r')})
    else:
        headerList = ['car_parking_machine', 'total_parking_fee']
        quickDict = {}
        for dict in listCheckout:
            quickDict[dict.get('cpm_name')] = float(dict.get('parking_fee').strip('\n').strip('\r')) + (
                quickDict.get('parking_fee') if dict.get('cpm_name') in quickDict.keys() else 0)
        csvListDict = [{'car_parking_machine':'cpm_' + k.lower(), 'total_parking_fee':v} for k,v in quickDict.items()]   
    writeToCSV(csvListDict, headerList)


def dictAllParked(in_date:str, out_date:str):
    listParked = {}
    listDict = []
    dRange, mRange, yRange = [range(int(i), 
        int(out_date.split('-')[in_date.split('-').index(i)]) + 1) for i in in_date.split('-')]
    with open(os.path.join(sys.path[0], 'carparklog.txt'), mode='r', newline='') as fileText:
        textFile = fileText.readlines()
        fileText.close()
    for line in textFile:
        dictLine = {v.split('=')[0]: v.split('=')[1] for v in ('date=' + line).split(';')}
        date = dictLine.get('date')[:10].split('-')
        if int(date[0]) in dRange and int(date[1]) in mRange and int(date[2]) in yRange:
            if not dictLine.get('action') == 'check-in' and dictLine.get('license_plate') in listParked:
                dictLine['date-in'] = listParked.get(dictLine.get('license_plate'))
                listDict.append(dictLine)
            else:
                listParked[dictLine.get('license_plate')] = dictLine.get('date')
    return listDict


def writeToCSV(listDict:list, fieldNames:list):
    with open(os.path.join(sys.path[0], 'carparkingreports.csv'), mode='w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=';')
        writer.writeheader()
        for dict in listDict:
            writer.writerow(dict)


def menuStructure():
    """[P] Report all parked cars during a parking period
[F] Report total collected parking fee during a parking period
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
        elif inp == 'Q':
            break
        else:
            print('invalid')

if __name__ == "__main__":
    main()
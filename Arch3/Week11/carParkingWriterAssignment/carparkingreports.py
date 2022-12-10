import sys
import os
import csv


def allParkedReport(in_date:str, out_date:list, machine:str=''):
    csvListDict = []
    headerList = []
    fileName = ''
    listCheckout = dictAllParked(in_date, out_date)
    if not machine == '':
        headerList = ["license_plate","check-in","check-out","parking_fee"]
        fileName = 'parkedcars_{}_from_{}_to_{}'.format(machine, in_date, out_date)
        for dict in listCheckout:
            if dict.get('cpm_name') == machine.lower().title():
                if not dict.get('date_in') == None:
                    csvListDict.append({'license_plate':dict.get('license_plate'), 'check-in':dict.get('date_in'), 
                        'check-out':dict.get('date'), 'parking_fee':dict.get('parking_fee') if not dict.get(
                            'parking_fee') == None else 0})
                else:
                    csvListDict.append({'license_plate':dict.get('license_plate'), 'check-in':dict.get('date'), 
                        'check-out':'None', 'parking_fee':dict.get('parking_fee') if not dict.get(
                            'parking_fee') == None else 0})
    else:
        headerList = ['car_parking_machine', 'total_parking_fee']
        quickDict = {}
        fileName = 'totalfee_from_{}_to_{}'.format(in_date, out_date)
        for dict in listCheckout:
            if not dict.get('parking_fee') == None:
                quickDict[dict.get('cpm_name')] = float(dict.get('parking_fee')) + (
                    quickDict.get('parking_fee') if dict.get('cpm_name') in quickDict.keys() else 0)
        csvListDict = [{'car_parking_machine':'cpm_' + k.lower(), 'total_parking_fee':v} for k,v in quickDict.items()]   
    writeToCSV(csvListDict, headerList, fileName)


def dictAllParked(in_date:str, out_date:str):
    listParked = {}
    listDict = []
    dRange, mRange, yRange = [range(int(i), 
        int(out_date.split('-')[in_date.split('-').index(i)]) + 1) for i in in_date.split('-')]
    with open(os.path.join(sys.path[0], 'carparklog.txt'), mode='r', newline='') as fileText:
        textFile = fileText.readlines()
        fileText.close()
    for line in textFile:
        line = line.rstrip('\r\n')
        dictLine = {v.split('=')[0]: v.split('=')[1] for v in ('date=' + line).split(';')}
        date = dictLine.get('date')[:10].split('-')
        if int(date[0]) in dRange and int(date[1]) in mRange and int(date[2]) in yRange:
            if not dictLine.get('action') == 'check-in' and dictLine.get('license_plate') in listParked:
                dictLine['date_in'] = listParked.get(dictLine.get('license_plate'))
                listDict.append(dictLine)
            else:
                listParked[dictLine.get('license_plate')] = dictLine.get('date')
                listDict.append(dictLine)
    return listDict


def writeToCSV(listDict:list, fieldNames:list, fileName:str):
    with open(os.path.join(sys.path[0], '{}.csv'.format(fileName)), mode='w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=';')
        writer.writeheader()
        for dict in listDict:
            writer.writerow(dict)


def menuStructure():
    """[P] Report all parked cars during a parking period for a specific parking machine
[F] Report total collected parking fee during a parking period for all parking machines
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
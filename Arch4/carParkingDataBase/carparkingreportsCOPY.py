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
        parked = listCheckout.copy()
        for dict_in in listCheckout:
            if dict_in.get('cpm_name') == machine.lower().title() and dict_in.get('action') == 'check-in':
                license = dict_in.get('license_plate')
                found = False
                for dict_out in parked:
                    if dict_out.get('license_plate') == license and dict_out.get('action') == 'check-out':
                        csvListDict.append({'license_plate':dict_out.get('license_plate'), 'check-in':dict_out.get('date_in'), 
                            'check-out':dict_out.get('date'), 'parking_fee':dict_out.get('parking_fee') if not dict_out.get(
                                'parking_fee') == None else 0})
                        found = True
                        parked.remove(dict_out)
                if found is False:
                    csvListDict.append({'license_plate':dict_in.get('license_plate'), 'check-in':dict_in.get('date'), 
                            'check-out':'None', 'parking_fee':dict_in.get('parking_fee') if not dict_in.get(
                                'parking_fee') == None else 0})
                parked.remove(dict_in)
    else:
        headerList = ['car_parking_machine', 'total_parking_fee']
        quickDict = {}
        quickFees = 0
        fileName = 'totalfee_from_{}_to_{}'.format(in_date, out_date)
        for dict in listCheckout:
            if not dict.get('parking_fee') == None:
                quickFees += float(dict.get('parking_fee'))
        quickDict[dict.get('cpm_name')] = quickFees
        csvListDict = [{'car_parking_machine': k.lower(), 'total_parking_fee':v} for k,v in quickDict.items()]   
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
            ...
        elif inp == 'Q':
            break
        else:
            print('invalid')

if __name__ == "__main__":
    main()
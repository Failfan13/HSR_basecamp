import requests
import sys
import os
import csv

# Load data from basecamp API : return dictionary with requested data
def dataLoader(get:str = 'team', symbol:str = '', history:str = ''):
    key = 'CxYTaRbXzO6x5B58'
    stdUrl = 'https://api.basecampcrypto.nl/v1/'
    if not symbol == '':
        symbol = f"/{symbol}"
    if not history == '':
        history = '/history'
    url = f"{stdUrl}{get}{symbol}{history}?key={key}"
    # error requesting http server (link does not exist)
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
    # error is reading stored csv file
    except requests.exceptions.HTTPError as err:
        # data sub folder or not
        try:
            with open(os.path.join(sys.path[0], "../crypto_daily_prices_365.csv"), mode="r") as cryptData:
                cryptData = [row.replace(';', ',') for row in cryptData.readlines()]
                dictCrypt = csv.DictReader(cryptData)
        except FileNotFoundError:
            with open(os.path.join(sys.path[0], "crypto_daily_prices_365.csv"), mode="r") as cryptData:
                cryptData = [row.replace(';', ',') for row in cryptData.readlines()]
                dictCrypt = csv.DictReader(cryptData)
        data = []
        # for every coin in header of csv file
        for key in dictCrypt.fieldnames:
            if not key.isnumeric():
                # if symbol is none or has value
                if symbol == '':
                    dataVal = {
                            'name': key,
                            'symbol': key[:3].upper(),
                            }
                    if not history == '':
                        dataVal['history'] = [{'day': dic.get('0'), 'value': dic.get(dataVal['name'])} for dic in dictCrypt]
                    data.append(dataVal)
                elif key.upper().find(symbol[1:]) >= 0:
                    dataVal = {
                            'name': key,
                            'symbol': key[:3].upper(),
                            }               
                    if not history == '':
                        dataVal['history'] = [{'day': dic.get('0'), 'value': dic.get(dataVal['name'])} for dic in dictCrypt]
                    data.append(dataVal)
    return data
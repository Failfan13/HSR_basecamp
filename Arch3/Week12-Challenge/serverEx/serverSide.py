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
            with open(os.path.join(sys.path[0], "../crypto_daily_prices_365.csv"), mode="rU") as cryptData:
                cryptData = [row.replace(';', ',') for row in cryptData.readlines()]
                dictCrypt = csv.DictReader(cryptData)
        except (IOError, OSError):
            with open(os.path.join(sys.path[0], "crypto_daily_prices_365.csv"), mode="rU") as cryptData:
                cryptData = [row.replace(';', ',') for row in cryptData.readlines()]
                dictCrypt = csv.DictReader(cryptData)
        data = {
                'name': list(filter(lambda x: symbol in x.upper(), next(dictCrypt).keys()))[0],
                'symbol': symbol,
                }
        if not history == '':
            data['history'] = [{'day': dic.get('0'), 'value': dic.get(data['name'])} for dic in dictCrypt]
    return data
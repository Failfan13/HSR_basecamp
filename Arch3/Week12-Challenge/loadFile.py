import sys
import os
import csv


def loadFile(file:str = 'crypto_daily_prices_365.csv'):
    try:
        with open(os.path.join(sys.path[0], file), mode='r', encoding='UTF-8') as textFile:
            return csv.DictReader(textFile)
    except (OSError, IOError):
        ...
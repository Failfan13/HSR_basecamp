from modules.modula import *
from tabulate import tabulate as table


def createTable(obj: object) -> None:
    obj.methodList = [obj.avg, obj.min_max, obj.stdDev, obj.qrtsYear, obj.range, obj.inQuRa, obj.upDown]
    table_data = [["", "AVG", "MIN", "MAX", "SD", "Q1", "Q2", "Q3", 
                    "RNG", "IQR", "UPS", "DOWNS", "LUP", "LDWN"]]
    lst = {i:[m(i) for m in obj.methodList] for i in obj.coins} 
    for coin, history in lst.items():
        valList = [f"{coin}"]
        for value in history:
            if isinstance(value, tuple):
                valList = valList + list(value)
            else:
                valList.append(value)
        table_data.append(valList)
    print(table(table_data, headers='firstrow', tablefmt='fancy_grid', floatfmt=".2f"))


def calcInvestment(obj: object):
    investors = {
        'alice': {
            'ivIn': 'ALB',
            'EURO': 1000000,
            'STOCK': 0,
            'BUY': lambda x: [i for i in x if i < 1500],
            'SELL': lambda x: [i for i in x if i > 1600]
        },
        'bob': {
            'ivIn': 'BHA',
            'EURO': 1000000,
            'STOCK': 0,
            'BUY': lambda x: [i for i in x if i < 1000],
            'SELL': lambda x: [i for i in x if i > 1100]
        },
        'carol': {
            'ivIn': 'CAS',
            'EURO': 1000000,
            'STOCK': 0,
            'BUY': lambda x: [v for ind, v in enumerate(x) if ind > 0 and ind < len(x)-1 and x[ind-1] > v < x[ind+1]],
            'SELL': lambda x: [v for ind, v in enumerate(x) if ind > 0 and ind < len(x)-1 and x[ind-1] < v > x[ind+1]]
        },
        'dave': {
            'ivIn': 'DUB',
            'EURO': 1000000,
            'STOCK': 0,
            'BUY': lambda x: [v for ind, v in enumerate(x) if (ind > 1 and (v <= x[ind-1] and x[ind-2]))],
            'SELL': lambda x: [v for ind, v in enumerate(x) if (ind > 1 and (v >= x[ind-1] and x[ind-2]))]
        },
        'eve': {
            'ivIn': 'ELG',
            'EURO': 1000000,
            'STOCK': 0,
            'BUY': lambda x: [v for ind, v in enumerate(x) if ind % 10 == 0],
            'SELL': lambda x: [v for ind, v in enumerate(x) if ind % 5 == 0 and ind % 10 != 0]
        },
        'frank': {
            'ivIn': 'FAW',
            'EURO': 1000000,
            'STOCK': 0,
            'BUY': lambda x: [v for ind, v in enumerate(x) if ind == 0 or (v / 100 * 80) > x[ind-1]],
            'SELL': lambda x: [v for ind, v in enumerate(x) if ind > 0 and (v / 100 * 120) > x[ind-1]]
        }
    }
    # print(investors.keys())
    for char in investors.keys():
        history = [val.get('value') for val in obj.history.get(investors.get(char).get('ivIn')).get('history')]
        for ind, value in enumerate(history):
            if investors.get(char).get('STOCK') == 0 and value in tuple(investors.get(char).get('BUY')(history[ind:])):
                investors[char]['STOCK'] = investors.get(char).get('EURO') // value
                investors[char]['EURO'] = investors.get(char).get('EURO') % value
            if investors.get(char).get('STOCK') > 0 and value in tuple(investors.get(char).get('SELL')(history[ind:])):
                investors[char]['EURO'] = investors.get(char).get('EURO') + (investors.get(char).get('STOCK') * value)
                investors[char]['STOCK'] = 0
            if ind == 364 and investors.get(char).get('STOCK') > 0:
                investors[char]['EURO'] = investors.get(char).get('EURO') + (investors.get(char).get('STOCK') * value)
                investors[char]['STOCK'] = 0


    print(investors['alice']['EURO'])
    print(investors['bob']['EURO'])
    print(investors['carol']['EURO'])
    print(investors['dave']['EURO'])
    print(investors['eve']['EURO'])
    print(investors['frank']['EURO'])


            
    # print(investors['carol']['SELL']())


def main():
    cC = calculateCoin()
    calcInvestment(cC)


if __name__ == "__main__":
    main()
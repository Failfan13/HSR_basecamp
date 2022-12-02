from serverEx.serverSide import dataLoader
from modules.modula import *
from tabulate import tabulate as table


def createTable(obj: object):
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


def main():
    cC = calculateCoin()
    #createTable(cC)


if __name__ == "__main__":
    main()
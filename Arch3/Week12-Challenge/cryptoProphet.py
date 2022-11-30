from serverSide import dataLoader as datLoad
from modula import *
import tabulate as table


def main():
    coinCal = calculateCoin()
    print(coinCal.up_down('DUB'))


if __name__ == "__main__":
    main()
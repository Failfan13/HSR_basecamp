from serverEx.serverSide import dataLoader as datLoad
import statistics as stat
import numpy as np

class calculateCoin():
    # initialiser
    def __init__(self) -> None:
        # list of all coins ['ALB', 'BHA' etc.
        self.coins = [data.get('symbol') for data in datLoad('coin')]
        # history of the coins above
        self.history = {c:datLoad(get='coin', symbol=c, history='ok') for c in self.coins}

    # calculate Average
    def avg(self, coin:str = 'ALB') -> float:
        history = self.history.get(coin).get('history')
        coinTot = sum(x.get('value') for x in history)
        return round(coinTot / len(history), 2)

    # calculate Min & Max
    def min_max(self, coin:str = 'ALB') -> tuple:
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history]
        return round(min(coinHis), 2), round(max(coinHis), 2)

    # calculate standard deviation
    def stdDev(self, coin:str = 'ALB') -> float:
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history]
        return round(stat.stdev(coinHis), 2)

    # Calculate median from q2 and total history in q1 and q3
    def qrtsYear(self, coin:str = 'ALB') -> tuple:
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history[90:181]]
        q3, q1 = np.percentile(coinHis, [75 ,25])
        coinHisQ2 = [x.get('value') for x in history[90:181]]
        return round(float(q1), 2), round(stat.median(coinHisQ2), 2), round(float(q3), 2)

    # calculate lagest difference between ups and downs
    def range(self, coin:str = 'ALB') -> float:
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history]
        return round((max(coinHis) - min(coinHis)), 2)

    # calculate average down up range
    def inQuRa(self, coin:str = 'ALB') -> float:
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history]
        coinHis.sort()
        q3, q1 = np.percentile(coinHis, [75 ,25])
        return round(float((q3 - q1)), 2)

    # calculate amount of ups and downs in history coin
    def upDown(self, coin:str = 'ALB') -> tuple:
        ups = downs = lUps = lDwns = countDown = countUp = 0
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history]
        for index, value in enumerate(coinHis):
            if index != 0:
                if value > coinHis[index - 1]:
                    countDown = 0
                    ups += 1
                    countUp += 1
                    if countUp > lUps:
                        lUps += 1
                if value <= coinHis[index - 1]:
                    countUp = 0
                    downs += 1
                    countDown += 1
                    if countDown > lDwns:
                        lDwns += 1
        return round(ups, 2), round(downs, 2), round(lUps, 2), round(lDwns, 2)
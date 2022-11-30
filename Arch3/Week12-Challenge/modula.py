from serverSide import dataLoader as datLoad
import statistics as stat
import numpy as np

class calculateCoin():
    def __init__(self) -> None:
        self.coins = [data.get('symbol') for data in datLoad('coin')]
        self.history = {c:datLoad(get='coin', symbol=c, history='ok') for c in self.coins}
        
    def avg(self, coin:str = 'ALB') -> str:
        history = self.history.get(coin).get('history')
        coinTot = sum(x.get('value') for x in history)
        return coinTot / len(history)

    def min_max(self, coin:str = 'ALB') -> str:
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history]
        return min(coinHis), max(coinHis)

    def std_dev(self, coin:str = 'ALB') -> str:
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history]
        return stat.stdev(coinHis)

    def qrtsYear(self, coin:str = 'ALB') -> str:
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history[90:181]]
        q3, q1 = np.percentile(coinHis, [75 ,25])
        coinHisQ2 = [x.get('value') for x in history[90:181]]
        return q1, stat.median(coinHisQ2), q3

    def range(self, coin:str = 'ALB') -> str:
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history]
        return (max(coinHis) - min(coinHis))

    def inQuRa(self, coin:str = 'ALB') -> str:
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history]
        coinHis.sort()
        q3, q1 = np.percentile(coinHis, [75 ,25])
        return (q3 - q1)

    def up_down(self, coin:str = 'ALB') -> str:
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
                
        return ups, downs, lUps, lDwns
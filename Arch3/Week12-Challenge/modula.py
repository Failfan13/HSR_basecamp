from serverSide import dataLoader as datLoad

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

    def std_dev(self, coin:str = 'ALB'):
        history = self.history.get(coin).get('history')
        coinHis = [x.get('value') for x in history]
        oksok = sum((x.get('value') - len(history))**2 for x in history) / len(history) ** 0.5
        print(oksok)


calculateCoin().std_dev()
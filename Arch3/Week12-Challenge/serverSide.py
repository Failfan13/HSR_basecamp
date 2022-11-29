import requests

# Load data from server with arguments to allocate different types of info
def dataLoader(get:str = 'team', symbol:str = '', history:str = ''):
    key = 'CxYTaRbXzO6x5B58'
    stdUrl = 'https://api.basecampcrypto.nl/v1/'
    if not symbol == '':
        symbol = f"/{symbol}"
    if not history == '':
        history = '/history'
    try:
        url = f"{stdUrl}{get}{symbol}{history}?key={key}"
    except ConnectionError:
        return 'invalid'
    r = requests.get(url)
    return r.json()
import requests

# Get data from server with assigned key
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
        print('invalid')
    r = requests.get(url)
    return r.json()
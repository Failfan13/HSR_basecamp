import requests

# Get data from server with assigned key
def dataLoader(get:str = 'team'):
    key = 'CxYTaRbXzO6x5B58'
    stdUrl = 'https://api.basecampcrypto.nl/v1/'
    try:
        url = f"{stdUrl}{get}?key={key}"
    except ConnectionError:
        print('invalid')
    r = requests.get(url)
    return r.json()
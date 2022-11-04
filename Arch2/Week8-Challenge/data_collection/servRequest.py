import requests
import json
import os
import sys

url = 'https://api.basecampserver.tech/sensors?node_id=658'

r = requests.get(url).text

if __name__ == '__main__':
    with open(os.path.join(sys.path[0], 'raspData.json'), 'w') as outfile:
        outfile.write(json.dumps(eval(r), indent=2))
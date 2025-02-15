import os

import requests
from dotenv import load_dotenv


load_dotenv()
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')

def get_gas_etherscan():
    url = f'https://api.etherscan.io/api'
    headers = {
        'accept': 'application/json'
    }
    params = {
        'module': 'gastracker',
        'action': 'gasoracle',
        'apikey': ETHERSCAN_API_KEY
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )
    if response.status_code == 200:
        res = response.json()
        return (True, res)
    else:
        return (False, 'Etherscan API is currently down. Please try again later.')


# --------------------     TEST        --------------------

# valid requests
# print(get_gas_etherscan())

import os

import requests
from dotenv import load_dotenv


load_dotenv()
BLOCKNATIVE_API_KEY = os.getenv('BLOCKNATIVE_API_KEY')

def get_gas_blocknative():
    url = f'https://api.blocknative.com/gasprices/blockprices'
    headers = {
        'accept': 'application/json',
        'Authorization': BLOCKNATIVE_API_KEY
    }
    params = {
        'chain_id': '137'
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
        return (False, 'Blocknative API is currently down. Please try again later.')


# --------------------     TEST        --------------------

# valid requests
# print(get_gas_blocknative())

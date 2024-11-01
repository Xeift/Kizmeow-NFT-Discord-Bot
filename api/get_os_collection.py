import os

import requests
from dotenv import load_dotenv

load_dotenv()
OPENSEA_API_KEY = os.getenv('OPENSEA_API_KEY')


def get_os_account(collection):
    url = f'https://api.opensea.io/api/v2/collections/{collection}'
    headers = {
        'accept': 'application/json',
        'x-api-key': OPENSEA_API_KEY
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        res = response.json()
        return (True, res)
    elif response.status_code == 400:
        return (False, 'The collection does not exist or can not be parsed.')
    else:
        return (False, 'OpenSea API is currently down. Please try again later.')


# --------------------     TEST        --------------------

# valid collection slug
res = get_os_account('azuki')
print(res)

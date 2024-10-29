import os

import requests
from dotenv import load_dotenv

load_dotenv()
OPENSEA_API_KEY = os.getenv('OPENSEA_API_KEY')


def get_os_account(account_name_or_address):

    url = f'https://api.opensea.io/api/v2/accounts/{account_name_or_address}'
    headers = {
        'accept': 'application/json',
        'x-api-key': OPENSEA_API_KEY
    }

    response = requests.get(url, headers=headers)

    print(response.text)


get_os_account('0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045')
# get_os_account('vitalik.eth')

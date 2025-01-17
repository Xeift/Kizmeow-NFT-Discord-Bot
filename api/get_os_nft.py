import os

import requests
from dotenv import load_dotenv

load_dotenv()
OPENSEA_API_KEY = os.getenv('OPENSEA_API_KEY')


def get_os_nft(address, chain, token_id):
    url = f'https://api.opensea.io/api/v2/chain/{chain}/contract/{address}/nfts/{token_id}'
    headers = {
        'accept': 'application/json',
        'x-api-key': OPENSEA_API_KEY
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        res = response.json()
        return (True, res)
    elif response.status_code == 400:
        err = response.json()['errors'][0]
        return (False, err)
    else:
        return (False, 'OpenSea API is currently down. Please try again later.')


# --------------------     TEST        --------------------

# valid info
print(get_os_nft(
    '0xbd3531da5cf5857e7cfaa92426877b022e612cf8',
    'ethereum',
    '5712'
))

# # invalid contract address
# print(get_os_nft(
#     '0xbd3531da5cf5857e7cfaa92426877b022e612cfg',
#     'ethereum',
#     '5712'
# ))

# invalid chain
# print(get_os_nft(
#     '0xbd3531da5cf5857e7cfaa92426877b022e612cf8',
#     'ethereu',
#     '5712'
# ))

# invalid token id
# print(get_os_nft(
#     '0xbd3531da5cf5857e7cfaa92426877b022e612cf8',
#     'ethereum',
#     '57129999'
# ))

import os

import requests
from dotenv import load_dotenv
from ens_to_address import ens_to_address

load_dotenv()
OPENSEA_API_KEY = os.getenv('OPENSEA_API_KEY')


def get_os_account(account_name_or_address):
    if account_name_or_address.endswith('.eth'):
        (success, account_name_or_address) = ens_to_address(account_name_or_address)
        if success == False:
            return (False, account_name_or_address)

    url = f'https://api.opensea.io/api/v2/accounts/{account_name_or_address}'
    headers = {
        'accept': 'application/json',
        'x-api-key': OPENSEA_API_KEY
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        res = response.json()
        return (True, res)
    elif response.status_code == 400:
        return (False, 'The account does not exist or can not be parsed.')
    else:
        return (False, 'OpenSea API is currently down. Please try again later.')


# --------------------     TEST        --------------------

# # valid address
# print(get_os_account('0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'))

# # invalid address
# print(get_os_account('0xf8dA6BF26964aF9D7eEd9e03E53415D37aA96045'))

# valid os username
# print(get_os_account('XeiftVault'))

# # invalid os username
# print(get_os_account('dasfre65_fsdh3r_64fsdfs'))

# # valid ens
# print(get_os_account('vitalik.eth'))

# # invalid ens
# print(get_os_account('vitaliktertert356666666666666666.eth'))

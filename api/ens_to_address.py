import os

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
WEB3_PROVIDER_URI = os.getenv('WEB3_PROVIDER_URI')


def ens_to_address(ens):
    w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))
    address = w3.ens.address(ens)

    if address:
        return address
    else:
        return False

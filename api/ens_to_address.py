import os

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
WEB3_PROVIDER_URI = os.getenv('WEB3_PROVIDER_URI')


def ens_to_address(ens):
    w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))
    address = w3.ens.address(ens)
    print(address)

    if address:
        return address
    else:
        return False


# res = ens_to_address('vitalik.eth')
res = ens_to_address('vitaliktertert356666666666666666.eth')
print(res)

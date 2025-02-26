import os

import json
import requests
from dotenv import load_dotenv


load_dotenv()
QUICKNODE_API_URI = os.getenv('QUICKNODE_API_URI')

def get_gas_quicknode():
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "qn_estimatePriorityFees",
        "params": {
            "last_n_blocks": 100,
            "account": "JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4",
            "api_version": 2
        }
    })
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(
        QUICKNODE_API_URI,
        headers=headers,
        data=payload
    )


    if response.status_code == 200:
        res = response.json()
        return (True, res)
    else:
        return (False, 'Quicknode API is currently down. Please try again later.')



# --------------------     TEST        --------------------

# valid requests
# print(get_gas_quicknode())

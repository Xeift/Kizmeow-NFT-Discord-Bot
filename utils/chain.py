import json

with open('chain_detail.json', 'r', encoding='utf-8') as file:
    chain_data = json.load(file)


def get_name_by_code(chain_code):
    return chain_data[chain_code]['chain_name']


def get_info_by_code(chain_code):
    single_chain_data = chain_data[chain_code]
    return (
        single_chain_data['chain_name'],
        single_chain_data['exp_name'],
        single_chain_data['exp_address_url'],
        single_chain_data['exp_token_url'],
        single_chain_data['exp_emoji'],
        single_chain_data['ticker'],
        single_chain_data['token_standards'],
    )


def get_code_by_name(chain_name):
    with open('chain_detail.json', 'r') as file:
        data = json.load(file)
    for k, v in data.items():
        if v['chain_name'] == chain_name:
            return k

# --------------------     TEST        --------------------
# print(get_name_by_code('ethereum'))

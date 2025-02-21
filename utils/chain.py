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
        single_chain_data['token_standards']
    )

def get_code_by_name(chain_name):
    for k, v in chain_data.items():
        if v['chain_name'] == chain_name:
            return k

def get_available_chains():
    return [v['chain_name'] for v in chain_data.values()]

def get_gas_source_by_name(chain_name):
    chain_code = get_code_by_name(chain_name)
    return chain_data[chain_code]['gas_source']

def get_gas_source_detail(chain_name, gas_source):
    chain_code = get_code_by_name(chain_name)
    gas_sources = chain_data[chain_code]['gas_source']
    return gas_sources.get(gas_source)

# --------------------     TEST        --------------------
# print(get_name_by_code('ethereum'))

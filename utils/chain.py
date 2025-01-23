import json

with open('chain_detail.json', 'r', encoding='utf-8') as file:
    chain_data = json.load(file)

def get_name_by_code(chain_code):
    return chain_data[chain_code]['chain_name']


# --------------------     TEST        --------------------
# print(get_name_by_code('ethereum'))

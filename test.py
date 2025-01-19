import json



def get_chain_code_from_name(chain_name):
    with open('chain_detail.json', 'r') as file:
        data = json.load(file)

    for k, v in data.items():
        if v['chain_name'] == chain_name: return k

def get_chain_name():
    with open('chain_detail.json', 'r') as file:
        data = json.load(file)
    return [v['chain_name'] for v in data.values()]

print(get_chain_code_from_name('Ethereum'))
print(get_chain_name())

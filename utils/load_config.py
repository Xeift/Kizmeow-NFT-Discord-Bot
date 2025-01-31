import json

default_data = {
    'button': False,
    'language': 'en-US',
    'visibility': True,
    'favorite_collections': {},
    'favorite_nfts': {}
}


def load_config_from_json(uid):
    with open('setting.json', 'r', encoding='utf-8') as file:
        setting_data = json.load(file)
        setting_data = setting_data.setdefault(
            uid, default_data
        )

    return (
        setting_data['button'],
        setting_data['language'],
        setting_data['visibility'],
        setting_data['favorite_collections'],
        setting_data['favorite_nfts']
    )


def update_config_to_json(
    uid,
    button=None,
    language=None,
    visibility=None,
    favorite_collections=None,
    favorite_nfts=None
):
    with open('setting.json', 'r', encoding='utf-8') as file:
        setting_data = json.load(file)
        setting_data[uid] = setting_data.setdefault(
            uid,
            default_data
        )
    if button != None:
        setting_data[uid]['button'] = button
    if language != None:
        setting_data[uid]['language'] = language
    if visibility != None:
        setting_data[uid]['visibility'] = visibility
    if favorite_collections != None:
        setting_data[uid]['favorite_collections'] = favorite_collections
    if favorite_nfts != None:
        setting_data[uid]['favorite_nfts'] = favorite_nfts

    with open('setting.json', 'w', encoding='utf-8') as file:
        json.dump(setting_data, file, ensure_ascii=False, indent=4)


# --------------------     TEST        --------------------
# print(load_config_from_json(('874806243208871977')))
# update_config_to_json('874806243208871977', button=True)

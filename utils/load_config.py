import json


def load_config_from_json(uid):
    with open('setting.json', 'r', encoding='utf-8') as file:
        setting_data = json.load(file)
        setting_data = setting_data.setdefault(
            uid,
            {
                'button': False,
                'language': 'en-US',
                'visibility': False
            }
        )

    return (
        setting_data['button'],
        setting_data['language'],
        setting_data['visibility']
    )


def update_config_to_json(
    uid,
    button=None,
    language=None,
    visibility=None
):
    with open('setting.json', 'r', encoding='utf-8') as file:
        setting_data = json.load(file)
        setting_data[uid] = setting_data.setdefault(
            uid,
            {
                'button': False,
                'language': 'en-US',
                'visibility': False
            }
        )
        print(setting_data)
        if button:
            setting_data[uid]['button'] = button
        if language:
            setting_data[uid]['language'] = language
        if visibility:
            setting_data[uid]['visibility'] = visibility

    with open('setting.json', 'w', encoding='utf-8') as file:
        json.dump(setting_data, file, ensure_ascii=False, indent=4)

# --------------------     TEST        --------------------
# print(load_config_from_json(('874806243208871977')))
# update_config_to_json('874806243208871977', button=True)

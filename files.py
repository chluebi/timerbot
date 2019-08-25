import json
import os

filepath = 'UserData'


def user_exists(user):
    if os.path.exists(f'{filepath}/{user.id}.json'):
        load_user(user.id)
        return
    else:
        save_user(user.id, {'name': str(user),
                            'id': user.id,
                            'timers': [],
                            'friends': []})
        return

def load_user(id):
    with open(f'{filepath}/{id}.json', 'r') as f:
        data = json.load(f)

    return data

def save_user(id,data):
    with open(f'{filepath}/{id}.json', 'w+') as f:
        json.dump(data, f, indent=4)


def load_users():
    end = {}
    for user in os.listdir(filepath):
        with open(f'{filepath}/{user}', 'r+') as f:
            end[user] = json.load(f)

    return end


def add_attribute(name, value):
    for user in os.listdir(filepath):
        with open(f'{filepath}/{user}', 'r+') as f:
            current = json.load(f)

        current[name] = value

        with open(f'{filepath}/{user}', 'w+') as f:
            json.dump(current, f, indent=4)


if __name__ == '__main__':
    add_attribute('friends', [])


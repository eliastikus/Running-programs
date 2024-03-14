import json

def save_data(user, opened_windows):
    try:
        with open('data.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    if user in existing_data:
        existing_data[user].extend(opened_windows)
    else:
        existing_data[user] = opened_windows

    with open('data.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

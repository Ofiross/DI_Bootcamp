import json


def load_database(src_file='static/background_colors.json'):
    with open(src_file, 'r') as color:
        data = json.load(color)
    return data

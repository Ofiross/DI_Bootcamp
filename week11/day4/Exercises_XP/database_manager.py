import json


def load_database(src_file='files/product_db.json'):
    with open(src_file, 'r') as products:
        data = json.load(products)
    return data

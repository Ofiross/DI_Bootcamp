import json


def retrieve_all_products(src_file='files/product_db.json'):
    with open(src_file, 'r') as products:
        all_products = json.load(products)
    return all_products


def retrieve_requested_product(product_id):
    products_data = products_data.retrieve_requested_product(product_id)
    requested_product = [
        dictionary for dictionary in products_data if dictionary["ProductId"] == product_id]

    return requested_product

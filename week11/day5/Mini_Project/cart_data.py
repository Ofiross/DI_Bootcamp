import json


def cart_items():
    with open('files/cart.json', 'r') as products:
        cart_products = json.load(products)
    return cart_products


def add_product():
    with open('files/cart.json', 'w') as products:
        added_products = json.load(products)
    return added_products

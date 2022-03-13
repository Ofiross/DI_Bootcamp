import json


def cart_items():
    with open('files/cart.json', 'r') as products:
        cart_products = json.load(products)
    return cart_products

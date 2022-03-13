from itertools import count
from flask import Flask, render_template, redirect, url_for
import products_data
import cart_data
import json

app = Flask(__name__)
products_data = products_data.retrieve_all_products()
cart_items = cart_data.cart_items()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/products')
def products():
    return render_template("products.html", products=products_data)


@app.route('/products/<product_id>')
def product_details(product_id):
    product_details = [
        dictionary for dictionary in products_data if dictionary["ProductId"] == product_id]

    return render_template("productDetail.html", product=product_details)


@app.route('/cart')
def cart():
    total = sum(price['Price'] for price in cart_items)
    item_in_cart = len(cart_items)
    return render_template("cart.html", cart_items=cart_items, no_items=(len(cart_items) == 0), total=total, items=item_in_cart)


@app.route('/add_product_to_cart/<product_id>')
def add_product(product_id):
    product_to_add = [
        dictionary for dictionary in products_data if dictionary["ProductId"] == product_id]
    with open('files/cart.json', "w") as file:
        json.dump(product_to_add, file)
    return redirect(url_for('products'))


@app.route('/delete_product_from_cart/<product_id>')
def delete_product(product_id):
    product_to_delete = [
        dictionary for dictionary in products_data if dictionary["ProductId"] == product_id]
    with open('files/cart.json', 'r') as products:
        cart = json.load(products)
    for product in cart:
        product.pop(product_to_delete)
    with open('files/cart.json', 'w') as data_file:
        data = json.dump(cart, data_file)
    return redirect()


if __name__ == "__main__":
    app.run(debug=True, port=5489)

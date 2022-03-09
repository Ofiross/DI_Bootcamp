from flask import Flask, render_template
import database_manager

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/products')
def products():
    products_data = database_manager.load_database()
    return render_template("products.html", products=products_data)


@app.route('/products/<product_id>')
def product_details(product_id):
    products_data = database_manager.load_database()
    product_details = [
        dictionary for dictionary in products_data if dictionary["ProductId"] == product_id]

    return render_template("productDetail.html", product=product_details)


if __name__ == "__main__":
    app.run(debug=True, port=5200)

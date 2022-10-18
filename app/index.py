from flask import render_template, request

from app import app
from app import dao


@app.route('/')
def index():
    category_id = request.args.get('category_id')


    categories = dao.load_categories()
    products = dao.load_products(category_id=category_id)

    return render_template('index.html', categories=categories, products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

import json, os
from app import app

def load_data(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)
def load_categories():
    return load_data(os.path.join(app.root_path, 'data/categories.json'))

def load_products(category_id=None):
    products = load_data(os.path.join(app.root_path, 'data/products.json'))

    if category_id:
        products = [p for p in products if p['category_id'] == int(category_id)]

    return products
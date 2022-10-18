import json, os
from app import app

def load_data(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)
def load_categories():
    return load_data(os.path.join(app.root_path, 'data/categories.json'))

def load_products():
    return load_data(os.path.join(app.root_path, 'data/products.json'))
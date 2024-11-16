from flask import Flask, render_template

app = Flask(__name__)

# Product data
products = {
    "montale": {
        "id": "montale",
        "name": "Montale Chocolate Greedy",
        "description": "Насыщенный аромат с яркими нотами шоколада и ванили.",
        "image": "montale.jpg",
        "options": [
            {"size": 2, "price": 2000},
            {"size": 5, "price": 4000},
            {"size": 10, "price": 7000}
        ]
    },
    "prada": {
        "id": "prada",
        "name": "Prada L'Homme",
        "description": "Элегантный и утончённый аромат с нотами нероли и амбры.",
        "image": "prada.jpg",
        "options": [
            {"size": 2, "price": 2500},
            {"size": 5, "price": 4500},
            {"size": 10, "price": 7500}
        ]
    },
    "jeanpaul": {
        "id": "jeanpaul",
        "name": "Jean Paul Gaultier Le Male Elixir",
        "description": "Мужской аромат с восточными и древесными нотами.",
        "image": "jeanpaul.jpg",
        "options": [
            {"size": 2, "price": 2300},
            {"size": 5, "price": 4300},
            {"size": 10, "price": 7300}
        ]
    }
}

@app.route('/')
def home():
    return render_template("products.html")

@app.route('/product/<product_id>')
def product_detail(product_id):
    product = products.get(product_id)
    if not product:
        return "Product not found", 404
    return render_template("product_detail.html", product=product)

if __name__ == '__main__':
    app.run(debug=True)

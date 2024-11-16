from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data
perfumes = [
    {"id": 1, "name": "Scent 1", "price": "$20", "image": "perfume1.jpg"},
    {"id": 2, "name": "Scent 2", "price": "$30", "image": "perfume2.jpg"},
]

wishlist = []

@app.route("/")
def index():
    return render_template("index.html", perfumes=perfumes)

@app.route("/wishlist", methods=["GET", "POST"])
def wishlist_view():
    if request.method == "POST":
        perfume_id = request.json.get("id")
        for perfume in perfumes:
            if perfume["id"] == perfume_id and perfume not in wishlist:
                wishlist.append(perfume)
    return render_template("wishlist.html", wishlist=wishlist)

if __name__ == "__main__":
    app.run(debug=True)

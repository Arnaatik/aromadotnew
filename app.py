from flask import Flask, render_template

app = Flask(__name__)

perfumes = [
    {"id": 1, "name": "Парфюм 1", "image": "perfume1.jpg"},
    {"id": 2, "name": "Парфюм 2", "image": "perfume2.jpg"},
    {"id": 3, "name": "Парфюм 3", "image": "perfume3.jpg"},
]

@app.route("/")
def index():
    return render_template("index.html", perfumes=perfumes)

if __name__ == "__main__":
    app.run(debug=True)

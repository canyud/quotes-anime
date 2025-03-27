from flask import Flask, render_template, request
import requests
from config import Config
from models import db
from resources import katanime_bp

app = Flask(__name__)

# Config Database (Jika menggunakan database)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///katanime.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Register API Blueprint
app.register_blueprint(katanime_bp, url_prefix="/api")

# Route untuk halaman utama
@app.route("/")
def home():
    url = f"{Config.BASE_URL}/getlistanime"
    response = requests.get(url)

    if response.status_code == 200:
        anime_list = response.json()["result"]
    else:
        anime_list = []

    return render_template("index.html", anime_list=anime_list)

# Route untuk menampilkan quotes dari anime tertentu
@app.route("/anime/<string:anime_name>")
def anime_quotes(anime_name):
    url = f"{Config.BASE_URL}/getbyanime?anime={anime_name}&page=1"
    response = requests.get(url)

    if response.status_code == 200:
        quotes = response.json()["result"]
    else:
        quotes = []

    return render_template("quotes.html", anime_name=anime_name, quotes=quotes)

# Route untuk mencari kata dalam quotes
@app.route("/carikata", methods=["GET"])
def cari_kata():
    kata = request.args.get("kata", "")  # Ambil parameter yang benar
    quotes = []

    if kata:
        url = f"{Config.BASE_URL}/carikata?kata={kata}&page=1"
        response = requests.get(url)

        if response.status_code == 200:
            quotes = response.json().get("result", [])

    return render_template("carikata.html", kata=kata, quotes=quotes)


if __name__ == "__main__":
    app.run(debug=True)

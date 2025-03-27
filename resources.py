import requests
from flask import Blueprint, jsonify, request
from config import Config

katanime_bp = Blueprint("katanime", __name__)

# Get random anime quote
@katanime_bp.route("/getrandom", methods=["GET"])
def get_random_quote():
    url = f"{Config.BASE_URL}/getrandom"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# Get list of anime
@katanime_bp.route("/getlistanime", methods=["GET"])
def get_list_anime():
    url = f"{Config.BASE_URL}/getlistanime"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# Get quotes by anime name (requires 'anime' and 'page' params)
@katanime_bp.route("/getbyanime", methods=["GET"])
def get_by_anime():
    anime_name = request.args.get("anime")
    page = request.args.get("page", type=int)

    if not anime_name or not page or page < 1:
        return jsonify({"error": "Parameters 'anime' and 'page' (>=1) are required"}), 400

    url = f"{Config.BASE_URL}/getbyanime?anime={anime_name}&page={page}"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

# Search anime quotes by keyword (requires 'kata' and 'page' params)
@katanime_bp.route("/carikata", methods=["GET"])
def search_quote():
    keyword = request.args.get("kata")
    page = request.args.get("page", type=int)

    if not keyword or not page or page < 1:
        return jsonify({"error": "Parameters 'kata' and 'page' (>=1) are required"}), 400

    url = f"{Config.BASE_URL}/carikata?kata={keyword}&page={page}"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

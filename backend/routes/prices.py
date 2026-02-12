from flask import Blueprint, request, jsonify
from services.price_service import get_prices

prices_bp = Blueprint("prices", __name__)

@prices_bp.route("/", methods=["GET"])
def fetch_prices():
    start_date = request.args.get("start")
    end_date = request.args.get("end")

    data = get_prices(start_date, end_date)
    return jsonify(data)

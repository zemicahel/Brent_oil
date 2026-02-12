from flask import Blueprint, jsonify
from services.changepoint_service import compute_change_point

changepoints_bp = Blueprint("changepoints", __name__)

@changepoints_bp.route("/", methods=["GET"])
def fetch_changepoints():
    result = compute_change_point()
    return jsonify(result)

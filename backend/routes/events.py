from flask import Blueprint, jsonify
from services.event_service import get_events

events_bp = Blueprint("events", __name__)

@events_bp.route("/", methods=["GET"])
def fetch_events():
    data = get_events()
    return jsonify(data)

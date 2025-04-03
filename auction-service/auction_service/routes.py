import requests
from flask import Blueprint, jsonify, request # type: ignore

auction_bp = Blueprint("auction_bp", __name__)

# Sample in-memory auctions data (in a real app, this would be in a database)
auctions = [
    {"id": 1, "title": "Antique Vase", "starting_bid": 100},
    {"id": 2, "title": "Vintage Car", "starting_bid": 5000},
]

@auction_bp.route("/")
def home():
    return jsonify({"message": "Auction Service is up and running!"})

@auction_bp.route("/auctions", methods=["GET"])
def list_auctions():
    return jsonify(auctions)

@auction_bp.route("/auctions", methods=["POST"])
def create_auction():
    data = request.get_json()
    title = data.get("title")
    starting_bid = data.get("starting_bid")
    if not title or starting_bid is None:
        return jsonify({"error": "Title and starting_bid are required"}), 400
    new_id = auctions[-1]["id"] + 1 if auctions else 1
    new_auction = {"id": new_id, "title": title, "starting_bid": starting_bid}
    auctions.append(new_auction)
    return jsonify(new_auction), 201

# Endpoint: Get user details from the User Service via HTTP call
@auction_bp.route("/user/<int:user_id>", methods=["GET"])
def get_user_details(user_id):
    try:
        # Call the User Service using its Docker Compose service name
        response = requests.get(f"http://user-service:5000/users/{user_id}")
        response.raise_for_status()
        user_data = response.json()
        return jsonify(user_data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch user details", "details": str(e)}), 500

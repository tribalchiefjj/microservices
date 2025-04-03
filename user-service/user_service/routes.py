from flask import Blueprint, jsonify, request # type: ignore
from flask_jwt_extended import ( # type: ignore
    JWTManager, create_access_token,
)
from .db import get_db_connection # type: ignore

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/")
def home():
    return jsonify({"message": "User Service is up and running!"})

@user_bp.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": row[0], "name": row[1], "email": row[2]} for row in rows])

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users WHERE id = %s;", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        return jsonify({"id": user[0], "name": user[1], "email": user[2]})
    else:
        return jsonify({"error": "User not found"}), 404



@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;", (name, email))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": user_id, "name": name, "email": email}), 201

# Login endpoint using JWT
@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    # Here you would normally validate credentials (e.g., password checking).
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    # For demonstration purposes, assume the email is valid.
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200


@user_bp.route("/users/<int:user_id>", methods=["PUT", "PATCH"])
def update_user(user_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    if not name and not email:
        return jsonify({"error": "At least one field (name or email) must be provided"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if email:
        fields.append("email = %s")
        values.append(email)
    values.append(user_id)
    query = f"UPDATE users SET {', '.join(fields)} WHERE id = %s RETURNING id, name, email;"
    cur.execute(query, tuple(values))
    updated_user = cur.fetchone()
    if not updated_user:
        conn.rollback()
        return jsonify({"error": "User not found"}), 404
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": updated_user[0], "name": updated_user[1], "email": updated_user[2]})

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s RETURNING id;", (user_id,))
    deleted = cur.fetchone()
    if not deleted:
        conn.rollback()
        return jsonify({"error": "User not found"}), 404
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": f"User {user_id} deleted"}), 200

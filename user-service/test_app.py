import os
import json
import pytest
from app import app  # Import your Flask app

@pytest.fixture
def client():
    # Set testing configuration
    app.config['TESTING'] = True
    # Override the DATABASE_URL to use localhost instead of "db"
    app.config['DATABASE_URL'] = "postgres db ***"
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "User Service is up" in data["message"]

def test_create_and_get_user(client):
    # Create a new user
    new_user = {"name": "Test User", "email": "test@example.com"}
    post_response = client.post("/users", json=new_user)
    assert post_response.status_code == 201
    created_user = json.loads(post_response.data)
    assert "id" in created_user

    user_id = created_user["id"]

    # Retrieve the user using the new endpoint
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    fetched_user = json.loads(get_response.data)
    assert fetched_user["name"] == new_user["name"]
    assert fetched_user["email"] == new_user["email"]

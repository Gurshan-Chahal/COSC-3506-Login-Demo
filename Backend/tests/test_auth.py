from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_login_success():

    response = client.post(
        "/api/login",
        json={
            "email": "student@example.com",
            "password": "Password123"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"


def test_login_wrong_password():

    response = client.post(
        "/api/login",
        json={
            "email": "student@example.com",
            "password": "WrongPassword"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Invalid email or password"


def test_login_unknown_user():

    response = client.post(
        "/api/login",
        json={
            "email": "unknown@example.com",
            "password": "Password123"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Invalid email or password"
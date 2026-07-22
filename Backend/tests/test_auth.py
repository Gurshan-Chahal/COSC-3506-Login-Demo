from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the Login Demo API!"
    }


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


def test_login_invalid_email():

    response = client.post(
        "/api/login",
        json={
            "email": "wrong@example.com",
            "password": "Password123"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Invalid email"


def test_login_invalid_password():

    response = client.post(
        "/api/login",
        json={
            "email": "student@example.com",
            "password": "WrongPassword"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Invalid password"


def test_login_empty_email():

    response = client.post(
        "/api/login",
        json={
            "email": "",
            "password": "Password123"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Email cannot be empty"


def test_login_empty_password():

    response = client.post(
        "/api/login",
        json={
            "email": "student@example.com",
            "password": ""
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Password cannot be empty"


def test_login_short_password():

    response = client.post(
        "/api/login",
        json={
            "email": "student@example.com",
            "password": "Pass1"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Password is too short"
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

def test_authorize():
    data = {"provider": "Garmin", "user_id": "user123"}
    response = client.post("/authorize", json=data)
    assert response.status_code == 200
    assert "device_id" in response.json()

def test_sync():
    data = {"provider": "Polar", "user_id": "user456"}
    response = client.post("/authorize", json=data)
    device_id = response.json()["device_id"]
    sync_response = client.post(f"/sync/{device_id}")
    assert sync_response.status_code == 200
    assert f"Sincronización iniciada para el dispositivo {device_id}" in sync_response.json()["message"]

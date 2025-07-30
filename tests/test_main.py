
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_say_hello():
    response = client.get("/hello/Kfir")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Kfir!"}

def test_echo():
    payload = {"key": "value"}
    response = client.post("/echo", json=payload)
    assert response.status_code == 200
    assert response.json() == {"received": payload}

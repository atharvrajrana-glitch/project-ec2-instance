from fastapi.testclient import TestClient
from app import app


client = TestClient(app)

def test_read_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message":"Hello, World!"}

def test_user_get():
    res = client.get("/users/5")
    print(res.json())
    data = res.json()
    assert data["id"] == 5
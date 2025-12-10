from fastapi.testclient import TestClient
from app.main import app
from app.auth import get_current_user

client = TestClient(app)

def test_read_users_me_override():
    def mock_user_provider():
        return {"username":"test_user", "role":"tester"}
    
    app.dependency_overrides[get_current_user] = mock_user_provider

    response = client.get("/users/me")

    assert response.status_code == 200
    assert response.json() == {"username":"test_user", "role":"tester"}

    app.dependency_overrides.clear()
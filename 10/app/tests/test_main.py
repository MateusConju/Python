from fastapi.testclient import TestClient
from app.main import app, is_workday

client = TestClient()

def testar_final_semana():
    app.dependency_override[is_workday] = lambda: False
    response = client.get("/work")
    assert response.json == {"statis": "partying"}
    app.dependency_overrides = {}
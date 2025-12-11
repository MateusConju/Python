import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core import security


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture
def user_token():
    token = security.create_access_token(
        subject="test_user",
        role="user"
    )
    return token


@pytest.fixture
def admin_token():
    token = security.create_access_token(
        subject="admin_user",
        role="admin"
    )
    return token

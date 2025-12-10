import pytest
from fastapi.testclient import TestClient
from app.core.database import engine, Base, SessionLocal, get_db
from app.main import app

@pytest.fixture(scope='session', autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    sessions = SessionLocal(bind=connection)

    yield sessions

    sessions.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session
    app.dependency.overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

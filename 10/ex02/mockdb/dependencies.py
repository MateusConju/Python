from .database import MockDB

def get_db():
    db = MockDB()
    db.connect()
    try:
        yield db
    finally:
        db.close()
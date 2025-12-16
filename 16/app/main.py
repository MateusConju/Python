from fastapi import FastAPI
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.api.v1.endpoints import auth, finances

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}", tags=['Auth'])
app.include_router(finances.router, prefix=f"{settings.API_V1_STR}", tags=['Finances'])

if __name__ == "__main__":
    from uvicorn import run
    run(app, host="0.0.0.0", port=80)
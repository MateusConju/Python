from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.api.v1.router import api_router

app = FastAPI(title="ShopFlow Capstone")

# Handler Global para Erros de Validação (Pydantic V2)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):

    errors = []

    for error in exc.errors():
        field = ".".join(str(x) for x in error["loc"])
        msg = error["msg"]
        errors.append(f"{field}: {msg}")

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "message": "Erro de validação nos dados enviados",
            "data": None,
            "meta": {"errors": errors}
        },
    )

app.include_router(api_router, prefix="/api/v1")

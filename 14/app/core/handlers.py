from fastapi import HTTPException, status, Request
from fastapi.responses import JSONResponse
from app.core.errors import StatusCodeNotFound

async def resource_not_found_handler(request:Request, exc:HTTPException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "type": "about:blank",
            "title": "Ops! O recurso solicitado não foi encontrado",
            "status": 404,
            "detail": f"O recurso solicitado na url {request.url.path} não foi encontrado, certifique-se que digitou corretamente e tente novamente!",
            "instance": request.url.path
        }
    )

async def status_not_found_handler(request:Request, exc:StatusCodeNotFound):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "type": "about:blank",
            "title": "O status code consultado não corresponde as opções cadastradas",
            "status": 404,
            "detail": exc.detail,
            "instance": request.url.path
        }
    )
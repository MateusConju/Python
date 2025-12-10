from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError 
from typing import List, Dict, Any

def _extract_validation_errors(exc: RequestValidationError) -> List[Dict[str, Any]]:
    invalid_params = []
    for error in exc.errors():
        field_path = ".".join(map(str, error["loc"][1:]))         
        invalid_params.append({
            "name": field_path,
            "reason": error["msg"]
        })
    return invalid_params

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    invalid_params = _extract_validation_errors(exc)
    
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "type": "about:blank",
            "title": "Um ou mais parâmetros inválidos.",
            "status": 400,
            "detail": "O Corpo da requisição contém parâmetros inválidos. Veja 'invalid_params'.",
            "instance": request.url.path,
            "invalid_params": invalid_params 
        }
    )
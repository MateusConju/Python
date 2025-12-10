from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app_03.core.exceptions import ResourceNotFoundException

app = FastAPI()

async def resource_not_found_handler(request:Request, exc:ResourceNotFoundException):
    # RFC 9457
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "type":"about:blank",
            "title":"Resource Not Found",
            "status":404,
            "detail":f"{exc.resource} com o id {exc.id} não foi encontrado!",
            "instance":request.url.path
        })

app.add_exception_handler(ResourceNotFoundException, resource_not_found_handler)

@app.get('/test404')
def test_404():
    raise ResourceNotFoundException("Mochila", 42)
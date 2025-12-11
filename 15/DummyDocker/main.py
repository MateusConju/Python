from fastapi import FastAPI, status

app = FastAPI()

@app.get('/')
async def main_page():
    return {"status":status.HTTP_200_OK, "msg":"Bem-Vindo!"}

@app.get('/hello')
async def hello_world():
    return {"status":status.HTTP_200_OK, "msg":"Olá, Mundo"}
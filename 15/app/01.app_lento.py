from time import sleep
from fastapi import FastAPI

app = FastAPI()

fake_db = {
    "games": [{"id":i, "name":f"Game - {i}"} for i in range(10000)]
}

@app.get('/heavy-games')
async def get_heavy_games():
    sleep(3)
    return {"data":fake_db['games'], "source":"database"}

@app.post('/send-mail')
async def process_email(email:str):
    sleep(5)
    return {"msg": f"Foi enviado um e-mail para {email}"}
from fastapi import FastAPI, status, HTTPException, Response

app = FastAPI()

@app.patch('/users/{uid}', status_code=status.HTTP_200_OK)
def update_user(uid:int):
    return Response(status_code=status.HTTP_200_OK)
    
@app.delete('/orders/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_order(id:int):
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.post('/users', status_code=status.HTTP_201_CREATED)
def add_user():
    return Response(status_code=status.HTTP_201_CREATED)

@app.get('/users/{uid}', status_code=status.HTTP_200_OK)
def get_user(uid:int):
    return Response(status_code=status.HTTP_200_OK)
    


'''
Dada a lista de endpoints:
POST /updateUser
GET /deleteOrder?id=5
GET /addUser?name=john&surname=doe
POST /returnUser/{uid}
'''
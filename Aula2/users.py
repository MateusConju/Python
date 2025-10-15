cache_users = []

def obter_usuario(user_id: int):
    if user_id in cache_users:
        print(f"Cache hit para user {user_id}")
        return cache_users[user_id]
    
    print(f"Cache Miss para user {user_id}")

    usuario = {
        "id" : user_id,
        "nome": f"Usuario {user_id}",
        "email": f"usuario{user_id}@example.com"
    }

    cache_users[user_id] = usuario
    return usuario

user1 = obter_usuario(123)
user2 = obter_usuario(123)
user3 = obter_usuario(123)

print(user1)
print(user2)
print(user3)
def main():
    user_id = 1001
    user_name = "Alice"
    email = "alice@example.com"
    conta_ativa = True
    tags = {"admin", "user"}
    perfil = criar_usuario(user_name, 30)

def criar_usuario(nome: str, idade: int) -> dict:
    return {"nome": nome, "idade": idade}

if __name__ == "__main__":
    main()

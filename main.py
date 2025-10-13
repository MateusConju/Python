def main():
    user_id = 1
    nome = "Mateus Keppke"
    email = "mateus.keppke@gmail.com"
    ativo = True
    tags = ["admin", "bahia", "python"]

    return {
        "id": user_id,
        "nome": nome,
        "email": email,
        "ativo": ativo,
        "tags": tags
    }


if __name__ == "__main__":
    usuario = main()
    print(usuario)

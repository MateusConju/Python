import timeit

def gerar_usuarios(n=1_000_000):
    usuarios = []
    for i in range(1, n + 1):
        nome = f"user_{i}"
        email = f"user_{i}@example.com"
        usuarios.append({
            "id": i,
            "nome": nome,
            "email": email
        })
    return usuarios


def criar_indices(usuarios):
    idx_id = {u["id"]: u for u in usuarios}
    idx_email = {u["email"]: u for u in usuarios}
    idx_nome = {u["nome"]: u for u in usuarios}
    return {"id": idx_id, "email": idx_email, "nome": idx_nome}


def buscar_usuario(criterio, valor, usuarios, indices):
    if criterio in indices:
        return indices[criterio].get(valor)
    else:
        for u in usuarios:
            if u.get(criterio) == valor:
                return u
    return None


usuarios = gerar_usuarios()
indices = criar_indices(usuarios)

id_teste = 500_000
email_teste = f"user_{id_teste}@example.com"
nome_teste = f"user_{id_teste}"

tempo_linear = timeit.timeit(
    lambda: buscar_usuario("id", id_teste, usuarios, {}),
    number=10
)

tempo_indexado = timeit.timeit(
    lambda: buscar_usuario("id", id_teste, usuarios, indices),
    number=10
)

print(f"Tempo busca linear: {tempo_linear:.6f} s")
print(f"Tempo busca com índice: {tempo_indexado:.6f} s")
print(f"Aceleração: {tempo_linear / tempo_indexado:.0f}x mais rápido!")

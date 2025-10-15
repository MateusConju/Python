# Dados de usuários de uma API externa
usuarios_api = [
    {"id": 1, "nome": "Ana", "idade": 28, "ativo": True},
    {"id": 2, "nome": "Bruno", "idade": 35, "ativo": False},
    {"id": 3, "nome": "Carla", "idade": 22, "ativo": True},
    {"id": 4, "nome": "Diego", "idade": 45, "ativo": True},
]

# 1 - Filtrar usuários ativos
nomes_ativos = [user["nome"] for user in usuarios_api if user["ativo"]]
print("Nomes ativos:", nomes_ativos)

# 2 - Dicionario de Id e nome
id_para_nome = {user["id"]: user["nome"] for user in usuarios_api}
print("ID para Nome:", id_para_nome)

# 3 Categorizar por faixa etária

def categorizar_idade(idade):
    if idade < 30:
        return "jovem"
    elif idade < 50:
        return "adulto"
    else:
        return "sênior"

categorias = {user["nome"]: categorizar_idade(user["idade"]) for user in usuarios_api}
print("Categorias por idade:", categorias)

# 4 Nested comprehension: Matriz de multiplicação

tabuada = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(tabuada[0][4])

# ❌ Complexo demais - prefira um for normal
resultado = [x for x in [y for y in [z for z in range(100) if z % 2 == 0] if y > 10] if x < 50]

# ✅ Melhor:
numeros = range(100)
pares = [n for n in numeros if n % 2 == 0]
filtrados = [n for n in pares if 10 < n < 50]
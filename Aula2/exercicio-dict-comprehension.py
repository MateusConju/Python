# Transforme uma lista de pedidos em um dicionário {cliente: total_gasto}, mas apenas para clientes com mais de R$ 100 em compras.
# pedidos = [
#     {"cliente": "Ana", "valor": 50.00},
#     {"cliente": "Bruno", "valor": 150.00},
#     {"cliente": "Ana", "valor": 80.00},  # Ana: 130 total
#     {"cliente": "Carlos", "valor": 30.00},
#     {"cliente": "Bruno", "valor": 50.00},  # Bruno: 200 total
# ]

# Desafio: Usar dict comprehension + sum()

pedidos = [
    {"cliente": "Ana", "valor": 50.00},
    {"cliente": "Bruno", "valor": 150.00},
    {"cliente": "Ana", "valor": 80.00},
    {"cliente": "Carlos", "valor": 30.00},
    {"cliente": "Bruno", "valor": 50.00},
]

resultado = {
    cliente: sum(p["valor"] for p in pedidos if p["cliente"] == cliente)
    for cliente in {p["cliente"] for p in pedidos}
    if sum(p["valor"] for p in pedidos if p["cliente"] == cliente) > 100
}

print(resultado)


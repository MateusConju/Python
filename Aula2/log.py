# Atividade
# Você tem uma lista de pedidos. Cada pedido é uma tupla: (id, cliente, valor, status). Extraia: (1) Pedidos pendentes, (2) Valor total, (3) Cliente com mais pedidos.
# pedidos = [
#     (1, "Ana", 150.00, "pago"),
#     (2, "Bruno", 200.00, "pendente"),
#     (3, "Ana", 100.00, "pago"),
#     (4, "Carlos", 300.00, "pendente"),
#     (5, "Ana", 50.00, "cancelado"),
# ]

# Desafio: Resolver em 5 minutos!
# Dica: Use compreensão de lista e função sum()

pedidos = [
    (1, "Ana", 150.00, "pago"),
    (2, "Bruno", 200.00, "pendente"),
    (3, "Ana", 100.00, "pago"),
    (4, "Carlos", 300.00, "pendente"),
    (5, "Ana", 50.00, "cancelado"),
]

pendentes = [p for p in pedidos if p[3] == "pendente"]

valor_total = sum(p[2] for p in pedidos)

from collections import Counter
cliente_mais_pedidos = Counter(p[1] for p in pedidos).most_common(1)[0][0]

print("Pedidos pendentes:", pendentes)
print("Valor total:", valor_total)
print("Cliente com mais pedidos:", cliente_mais_pedidos)

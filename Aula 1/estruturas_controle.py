# idade = 18

# if idade >= 18:
#     print("Você é maior de idade")
# elif idade >= 16:
#     print("Voce2 é menor de idade mas pode votar")
# else:
#     print("Você é menor de idade e não pode votar")

# nomes = ["Ana", "Bruno", "Carlos"]
# for nome in nomes:
#     print(nome)

# contador = 5
# while contador > 5:
#     print(contador)
#     contador -= 1

# **Exercício: Classificador de Performance**

# **Briefing:**

# > "Você recebe uma lista de tempos de resposta de uma API (em ms). Classifique cada tempo como: 'Excelente' (<100ms), 'Bom' (100-300ms), 'Aceitável' (300-1000ms), 'Lento' (>1000ms)."
# >

# Esqueleto inicial:
tempos_resposta = [50, 120, 450, 1200, 80, 950]

# DESAFIO: Use for + if/elif/else para classificar
# Saída esperada:
# 50ms: Excelente
# 120ms: Bom
# ...

for tempo in tempos_resposta:
    if tempo < 100:
        classificacao = 'Excelente'
    elif tempo < 300:
        classificacao = 'Bom'
    elif tempo <= 1000:
        classificacao = 'Aceitável'
    else:
        classificacao = 'Lento'
    
    print(f"{tempo}ms: {classificacao}")

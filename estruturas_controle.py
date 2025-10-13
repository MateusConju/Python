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

tempos_resposta = [50, 120, 450, 1200, 80, 950]

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

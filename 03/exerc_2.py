def processar_notas(notas: list):
    menor = min(notas)
    notas.remove(menor)
    
    media = sum(notas) / len(notas)
    return media

notas = [7.5, 9.0, 6.0, 8.0]
resultado = processar_notas(notas)
print("Média das notas:", resultado)

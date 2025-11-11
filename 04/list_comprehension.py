def jeito_antigo(numeros:list) -> list:
    final = []
    for n in numeros:
        if n % 2 == 0:
            final.append(n * n)
    return final

def jeito_novo(numeros:list) -> list:
    return [n * n # Valor incrementado == parte de dentro do For Loop
            for n in numeros # Laço de repetição | For Loop
            if n % 2 == 0] # Condicional | Opcional na LC

if __name__ == '__main__':
    lista_numeros = list( # Transformar em lista
                        range( # Iterar pelos números de 0 até n
                            int( # Transforma valor em inteiros
                                input('Digite um número:\n> ') # Pega um valor do usuário
                            )))
    antigo = jeito_antigo(lista_numeros)
    print(f'Modo Antigo: {antigo}')

    novo = jeito_novo(lista_numeros)
    print(f'Modo Novo: {novo}')

    quadrado_todos = [n * n for n in lista_numeros]
    print(quadrado_todos)
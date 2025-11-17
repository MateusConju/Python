'''
 ________
|> EX01 <|
Crie uma função chamada calcular_media que receba uma lista de números (inteiros ou floats) 
e retorne a média. A função deve ter type hints (anotações de tipo) corretos para os argumentos e para 
o valor de retorno.

Bônus: Se a lista estiver vazia, a função deve retornar 0.0 (Float).
'''

def calcular_media(numeros:list[int]) -> float:
    '''
    Essa função calcula a média de uma lista

    Retorno
    -------
    A função retorna um [float]

    Exemplo
    -------
    >>> lista_notas:list = [5,8,9,9,7,8]
    >>> calcular_media(lista_notas)
    > Output >>> 7.66
    '''
    if not bool(numeros): return 0.0
    total:float = 0.0
    for n in numeros:
        total += n
    return total / len(numeros)

print(calcular_media([10,0]))
print(calcular_media([5,8,9,9,7,8]))
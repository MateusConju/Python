from time import time
def buscar(lista:list, alvo:int) -> any:
    for elemento in lista:
        if elemento == alvo:
            return True
    return False

small = list(range(10000))
big = list(range(80000))

n = input('Digite o seu número:\n> ')

start = time()
buscar(small, n)
end = time()
print(f'{'Small :':10} {end-start}')

start = time()
buscar(big, n)
end = time()
print(f'{'Big :':10} {end-start}')

from time import sleep, time

lista_grande = list(range(1,1000001))
n = int(input('Digite um numero:\n> '))

def bigode_nn(n):
    for i in range(n):
        lista_grande.pop(0)

def bigode_n(n):
    nova_lista = lista_grande[n:]
    return nova_lista

print('Bigode N**N')
sleep(2)
print('Iniciando em... 3', end='\r')
sleep(1)
print('Iniciando em... 2', end='\r')
sleep(1)
print('Iniciando em... 1')
sleep(1)
start = time()
bigode_nn(n)
end = time()

print(f'Pronto! -> Elapsed Time: {end-start}')

print('Bigode N')
sleep(2)
print('Iniciando em... 3', end='\r')
sleep(1)
print('Iniciando em... 2', end='\r')
sleep(1)
print('Iniciando em... 1')
sleep(1)

start = time()
lista = bigode_n(n)
end = time()

print(f'Pronto! -> Elapsed Time: {end-start}')

from time import time
def first(lista:list) -> any:
    return lista[0]

small = [10, 20, 30]
big = list(range(1000000))


start = time()
first(small)
end = time()
print(f'Small : {end-start}')

start = time()
first(big)
end = time()
print(f'Big : {end-start}')

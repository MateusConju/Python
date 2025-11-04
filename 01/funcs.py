global CONTADOR

def increment(num:int) -> None:
    CONTADOR = 0
    cont = CONTADOR
    for i in range(num):
        cont +=1
    CONTADOR = cont

    print(cont)

def argumentos(inteiro:int, texto:str) -> dict:
    return {'inteiro': inteiro, 'texto': texto}

if __name__ == '__main__':
    args = argumentos(inteiro=1000000, texto='Milhão')
    print(type(args))
    print(args)
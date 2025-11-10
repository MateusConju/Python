def checkar_par_antigo(n:int):
    if n% 2 == 0:
        return 'Par'
    else: 
        return 'Impar'
    
def checkar_par(n:int):
    return 'par' if n % 2 == 0 else 'impar'
    

if __name__ == '__main__':
    try:
        while True:
            num = int(input('Digite o seu numero:\n> '))
            print(f'O numero {num} é {checkar_par(num)}')
    except KeyboardInterrupt:
        print('Terminado pelo usuario!')
        exit()


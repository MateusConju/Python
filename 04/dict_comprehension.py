lista_nomes:list = ['joão', 'maria', 'roberto', 'claudia', 'patricia', 'fabio']

teste:str = lista_nomes[0]
teste2:list = teste[-1]

dict_masculino = {nome:'Masculino' for nome in lista_nomes if nome[-1] == 'o'}
dict_feminino = {nome:'Feminino' for nome in lista_nomes if nome[-1] == 'a'}

print(f'{dict_masculino = }')
print(f'{dict_feminino = }')

# Retornar numeros pares de 1 até n
print([n for n in range(1,int(input('Digite um número:\n> ')) +1 ) if n % 2 == 0])

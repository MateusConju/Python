import os

# Numericos
inteiro:int = 0
flutuante:float = 42.0

# Texto
texto_simples:str = 'Qualquer coisa'
texto_bytes:bytes = b'Qualquer coisa'

# Nulo
nada:None = None

# Bolleano
Verdadeiro:bool = True
falso:bool = False

# Coleções
lista:list = ['Meu nome', 24, False, None, b'ByteSting']
tupla:tuple = ('abc', 12)
lista_set:set = {'abc', 2, 3}
dicionario:dict = {'abc':1, 2:3}

variavel:any = None
variavel = flutuante

# Limpando o Terminal
os.sistem('clear')

print(variavel)
print(type(variavel))
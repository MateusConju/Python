lista_teste = [1,2,3,4,5]

lista_teste.pop() # O(1)
lista_teste.append(5) # O(1)

if 6 in lista_teste: print('Tem!') # O(n)

lista_teste.insert(0,0) # O(n)

print(lista_teste)

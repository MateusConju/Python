'''
 ________
|> EX02 <|
Crie uma função:

>>> classificar_imc(peso: float, altura: float) -> str. 

A função deve primeiro calcular o IMC (Índice de Massa Corporal) usando a fórmula:

>>> $peso / (altura * altura)$

Em seguida, deve retornar uma string classificando o resultado:

- Menor que 18.5: "Abaixo do peso"
- 18.5 a 24.9: "Peso normal"
- 25.0 a 29.9: "Sobrepeso"
- 30.0 ou mais: "Obesidade"
'''

def classificar_imc(
        peso:float,
        altura:float
        ) -> str:
    valores_imc = [(18.5,'Abaixo do peso'),(25,'Peso normal'),(30,'Sobrepeso')]
    
    num_imc = peso / (altura * altura)

    for valor in valores_imc:
        if num_imc < valor[0]:
            return valor[1]
    return 'Obesidade'

print(classificar_imc(423,1.7))

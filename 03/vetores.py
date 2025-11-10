class VetorZero(ZeroDivisionError):

    def __init__(self, *args):
        super().__init__(*args)

class Vetor2D:

    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Vetor2D(x={self.x}, y={self.y})'

    def __add__(self, other):
        final = self.validar_valor(other)

        valor_vetor = (self.x + final[0], self.y + final[1])

        return Vetor2D(valor_vetor[0], valor_vetor[1])
    
    def __sub__(self,other):
        final = self.validar_valor(other)

        valor_vetor = (
            self.x - final[0] # Valor se verdadeiro
            if self.x - final[0] > 0 # Condicional
            else # Delimitador de Condicional
            0 # Valor se falso
            , # Separador
            self.x - final[1]
            if self.x - final[1] > 0
            else
            0
            )

        return Vetor2D(valor_vetor[0], valor_vetor[1])
    
    def __mul__(self,other):
        final = self.validar_valor(other)

        valor_vetor = (self.x * final[0], self.y * final[1])

        return Vetor2D(valor_vetor[0], valor_vetor[1])
    
    def __truediv__(self,other):
        final = self.validar_valor(other)
        
        if final[0] == 0 or final[1] == 0:
            raise VetorZero('Um vetor não pode ser dividido por 0!')

        valor_vetor = (self.x / final[0], self.y / final[1])
        
        return Vetor2D(valor_vetor[0], valor_vetor[1])

    def validar_valor(self, other):
        final = None
        if isinstance(other, Vetor2D):
            final = [other.x, other.y]
        elif isinstance(other, int):
            final = [other, other]
        elif isinstance(other, tuple):
            final = other
        else:
            raise Exception('Operação não suportada!\nOs valores da operação estão incorretos!')
        
        if final is None: raise Exception('Ocorreu um erro na validação de valores!')
        else: return final 

if __name__ == '__main__':
    v1 = Vetor2D(x=3, y=4)
    v2 = Vetor2D(x=1, y=2)

    print(f'{v1 = }')
    print(f'{v2 = }')

    print(f'v1 + v2 = {v1 + v2}') # Vetor2D(x=4, y=6)
    #print(f'v1 + 5 = {v1 + 5}') # Vetor2D(x=8, y=9)
    #print(f'v1 + (3,2) = {v1 + (3,2)}') # Vetor2D(x=6, y=6)
    #print(f'v1 + (2) = {v1 + (2)}') # Vetor2D(x=6, y=6)

    print(f'v2 - v1 = {v2 - v1}') # Vetor2D(x=0, y=0)

    print(f'v1 * 5 = {v1 * 5}') # Vetor2D(x=15, y=20)

    print(f'v2 / (v2 - v1) = {v2 / (v2 - v1)}') # Erro Div por 0

    # DRY
    # -=-=-=-=
    # Don't
    # Repeat
    # Yourself

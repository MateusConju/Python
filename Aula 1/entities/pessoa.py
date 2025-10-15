class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf # Atributo privado 
        # self.__cpf = cpf # Atributo fortemente privado

    @property
    def cpf(self) -> str:
        return self._cpf
    
    @cpf.setter
    def cpf(self, valor: str) -> None:
        if len(valor) == 11 and valor.isdigit():
            self._cpf = valor
        else:
            raise ValueError("CPF deve conter 11 dígitos numéricos.")   

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
    def __str__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idade}"

    def __repr__(self) -> str:
        return f"Pessoa(nome={self.nome!r}, idade={self.idade!r})"

if __name__ == "__main__":
    pessoa = Pessoa("João", 30, "12345678901")
    print(pessoa.apresentar())
    # pessoa.cpf = "109876543"
    # print(pessoa)

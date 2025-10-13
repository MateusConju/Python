class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self._cpf = cpf  # usa o atributo privado

    @property
    def cpf(self) -> str:
        return self._cpf
    
    @cpf.setter
    def cpf(self, valor: str):
        # valida se o CPF tem 11 dígitos e se é numérico
        if not isinstance(valor, str):
            raise TypeError("O CPF deve ser uma string.")
        if len(valor) != 11 or not valor.isdigit():
            raise ValueError("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
        
        self._cpf = valor

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
    def __str__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idade}"
    
    def __repr__(self) -> str:
        return f"Pessoa(nome={self.nome!r}, idade={self.idade!r}, cpf={self._cpf!r})"
    
if __name__ == "__main__":
    pessoa = Pessoa("João", 35, "12345678901")
    print(pessoa.apresentar())

    pessoa.idade = 31
    print(pessoa)

    try:
        pessoa.cpf = "abc123"
    except ValueError as e:
        print(f"Erro: {e}")

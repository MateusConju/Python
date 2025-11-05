class Leitura:
    def __init__(self, nome: str):
        self.nome = nome
        self.abacate = False
        self.abacaxi = False

    def __enter__(self):
        print("Entrou no contexto!")
        return self

    def __exit__(self, a, b, c):
        print("Saiu do contexto:", a, b, c)

    def __repr__(self):
        return f"Leitura(nome={self.nome!r}, abacate={self.abacate}, abacaxi={self.abacaxi})"

with Leitura("arquivo.txt") as leitura:
    print("Dentro do with")
    print(leitura)
    leitura.abacate = True

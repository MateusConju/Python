# carstorechallenge/models.py

class Carro:
    """
    Representa um carro na concessionária.

    Atributos:
        `id` (str): O identificador único do carro.
        `modelo` (str): O modelo do carro.
        `marca` (str): A marca do carro.
        `ano` (int): O ano de fabricação do carro.
        `valor_base` (float): O valor base do carro.
        `condicao` (str): A condição do carro (Novo, Usado, etc.).
    """
    def __init__(self, id, modelo, marca, ano, valor_base, condicao):
        '''
        TODO
        ----
        Inicialize os atributos da classe Carro com os valores recebidos.
        '''
        self.id = id
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.valor_base = float(valor_base)
        self.condicao = condicao


class Concessionaria:
    """
    Representa a concessionária que gerencia os carros.

    Atributos:
        `nome` (str): O nome da concessionária.
        `carros` (list): A lista de carros (objetos da classe Carro) na concessionária.
    """
    def __init__(self, nome):
        '''
        TODO
        ----
        Inicialize o nome e a lista de carros (vazia).
        '''
        self.nome = nome
        self.carros = []

    def adicionar_carro(self, carro):
        """
        Adiciona um carro à lista da concessionária.

        TODO
        ----
        Implemente a lógica para adicionar um carro à lista 'self.carros'.
        """
        if not isinstance(carro, Carro):
            raise TypeError("adicionar_carro espera um objeto da classe Carro")
        self.carros.append(carro)

    def calcular_preco_venda(self, carro):
        """
        Calcula o preço de venda de um carro com base na sua condição.

        Regras:
        - Novo: `valor_base` + 20%
        - Usado: `valor_base` - 30%
        - Recondicionado: `valor_base` - 40%
        - Avariado: `valor_base` - 55%
        """
        cond = carro.condicao.lower()
        valor = float(carro.valor_base)

        if cond == "novo":
            preco = valor * 1.20
        elif cond == "usado":
            preco = valor * 0.70
        elif cond == "recondicionado":
            preco = valor * 0.60
        elif cond == "avariado":
            preco = valor * 0.45
        else:
            raise ValueError(f"Condição desconhecida: {carro.condicao}")

        return round(preco, 2)

    def gerar_relatorio_carro(self, carro):
        """
        Gera uma string formatada com o relatório de um carro específico.
        """
        preco_venda = self.calcular_preco_venda(carro)

        return (
            "--- Relatório do Veículo ---\n"
            f"Modelo: {carro.modelo} ({carro.ano})\n"
            f"Marca: {carro.marca}\n"
            f"Condição: {carro.condicao}\n"
            f"Valor Base: R$ {carro.valor_base:,.2f}\n"
            f"Preço de Venda: R$ {preco_venda:,.2f}\n"
            "--------------------------"
        )

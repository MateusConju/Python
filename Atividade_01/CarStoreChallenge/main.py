# main.py

# Importe as classes Carro e Concessionaria
from carstorechallenge.models import Carro, Concessionaria

def main():
    """
    Função principal para executar o desafio CarStore.
    """
    print("Iniciando o Desafio da Concessionária...\n")

    # 1) Criar a concessionária
    minha_concessionaria = Concessionaria(nome="Super Car")

    # 2) Dados simulados da API
    dados_api_1 = {
        "id": "f7e6e8b5-5a3c-4b0f-8d7a-9c1e0b9b0e4a",
        "modelo": "Tesla Model S",
        "marca": "Tesla",
        "ano": 2023,
        "valor_base": 1587865.22,
        "condicao": "Novo"
    }

    dados_api_2 = {
        "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
        "modelo": "Lamborghini Revuelto",
        "marca": "Lamborghini",
        "ano": 2025,
        "valor_base": 4867905.37,
        "condicao": "Avariado"
    }

    dados_api_3 = {
        "id": "6a7b8c9d-0e1f-2345-6789-012345fedcba",
        "modelo": "Hyundai Hb20",
        "marca": "Hyundai",
        "ano": 2025,
        "valor_base": 109990.00,
        "condicao": "Usado"
    }

    # 3) Criar instâncias de Carro usando os dados da API
    carro1 = Carro(**dados_api_1)
    carro2 = Carro(**dados_api_2)
    carro3 = Carro(**dados_api_3)

    # 4) Adicionar os carros à concessionária
    minha_concessionaria.adicionar_carro(carro1)
    minha_concessionaria.adicionar_carro(carro2)
    minha_concessionaria.adicionar_carro(carro3)

    # 5) Imprimir relatórios individuais
    print(minha_concessionaria.gerar_relatorio_carro(carro1))
    print()
    print(minha_concessionaria.gerar_relatorio_carro(carro2))
    print()
    print(minha_concessionaria.gerar_relatorio_carro(carro3))
    print()

    # 6) Desafio Extra – relatório geral
    print("=== RELATÓRIO GERAL ===\n")
    for carro in minha_concessionaria.carros:
        print(minha_concessionaria.gerar_relatorio_carro(carro))
        print()


if __name__ == "__main__":
    main()

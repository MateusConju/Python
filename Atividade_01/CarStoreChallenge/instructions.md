# Exercício 1: Desafio da Concessionária (CarStore Challenge)

## Objetivo

Seu desafio é criar um sistema em Python para gerenciar os carros de uma concessionária. O sistema deverá ser capaz de registrar carros com base em dados "vindos de uma API" e calcular seu preço de venda com base em sua condição (Novo, Usado, etc.).

Este exercício testará seus conhecimentos em **Orientação a Objetos (OOP)**, manipulação de dados e organização de projetos em Python.

## Conceitos a serem aplicados
- Criação de Classes e Objetos (`Carro`, `Concessionaria`).
- Métodos de classe e de instância.
- Encapsulamento de lógica de negócio.
- Manipulação de dicionários e listas.
- Formatação de strings e saídas no console.

## Simulação da API

Para este exercício, não usaremos uma API real. Em vez disso, você vai simular a resposta de uma API usando o dicionário Python abaixo. Imagine que seu script fez uma requisição `GET` e recebeu estes dados:

```python
dados_api_1 = {
    "id": "f7e6e8b5-5a3c-4b0f-8d7a-9c1e0b9b0e4a", # UUID
    "modelo": "Tesla Model S",
    "marca": "Tesla",
    "ano": 2023,
    "valor_base": 1587865.22,
    "condicao": "Novo" # Pode ser: Novo, Usado, Recondicionado, Avariado
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
```

## Requisitos

Você deve criar duas classes principais dentro do módulo `carstorechallenge/models.py`:

### 1. Classe `Carro`
Esta classe representará um carro individual.
- **Atributos:**
    - `id` (str): Identificador único do carro.
    - `modelo` (str): Modelo do carro.
    - `marca` (str): Marca do carro.
    - `ano` (int): Ano de fabricação.
    - `valor_base` (float): Valor do carro vindo da "API".
    - `condicao` (str): A condição atual do carro.

### 2. Classe `Concessionaria`
Esta classe gerenciará a coleção de carros e a lógica de preços.
- **Atributos:**
    - `nome` (str): Nome da concessionária.
    - `carros` (list): Uma lista para armazenar as **instâncias** da classe `Carro`.
- **Métodos:**
    - `__init__(self, nome)`: Construtor que define o nome da concessionária e inicializa a lista de carros vazia.
    - `adicionar_carro(self, carro)`: Adiciona uma instância de `Carro` à lista `carros`.
    - `calcular_preco_venda(self, carro)`: **Este é o método principal!** Ele recebe um objeto `Carro` e retorna o preço final de venda com base na sua `condicao`, seguindo as regras:
        - **Novo:** `valor_base` + 20%
        - **Usado:** `valor_base` - 30%
        - **Recondicionado:** `valor_base` - 40%
        - **Avariado:** `valor_base` - 55% (usaremos um valor fixo para simplificar)
    - `gerar_relatorio_carro(self, carro)`: Recebe um objeto `Carro`, calcula seu preço de venda usando o método acima e retorna uma string formatada com um resumo do carro. Exemplo:
        ```
        --- Relatório do Veículo ---
        Modelo: Tesla Model S Plaid (2023)
        Marca: Tesla
        Condição: Novo
        Valor Base: R$ 1.587.865,22
        Preço de Venda: R$ 1.905.438,26
        --------------------------
        ```

## Passo a Passo Sugerido

1.  **Defina as Classes:** Vá para o arquivo `carstorechallenge/models.py` e crie as classes `Carro` e `Concessionaria` com os atributos e métodos descritos.
2.  **Implemente a Lógica:** Preencha a lógica dos métodos, especialmente `calcular_preco_venda`.
3.  **Use as Classes:** No arquivo `main.py`:
    a. Importe as classes que você criou.
    b. Crie uma instância da `Concessionaria`.
    c. Use os `dados_api` (o dicionário) para criar uma instância da classe `Carro`.
    d. Adicione o carro à concessionária.
    e. Gere e imprima o relatório do carro no console.

## Desafio Extra (Opcional)

Modifique o sistema para que a `Concessionaria` possa ter vários carros. Crie um método `gerar_relatorio_geral(self)` que itera por todos os carros na lista e imprime o relatório de cada um. Teste com diferentes condições de veículos.

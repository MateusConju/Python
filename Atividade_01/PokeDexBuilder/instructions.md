# Exercício 2: Construtor de Pokédex (PokeDex Builder)

## Objetivo

Seu objetivo é criar um programa que consome a [PokéAPI](https://pokeapi.co/), uma API pública e gratuita com dados do universo Pokémon. Você irá buscar as informações de um Pokémon, armazená-las em objetos e gerenciá-las em uma Pokédex.

Este exercício é focado no uso da biblioteca `requests` para fazer chamadas `GET` a uma API externa e na conversão de dados JSON em objetos Python.

## Conceitos a serem aplicados
- Requisições HTTP com a biblioteca `requests`.
- Tratamento de respostas JSON.
- Criação de Classes e Objetos (`Pokemon`, `Pokedex`).
- Manipulação de listas e dicionários extraídos de uma API.
- List Comprehension (sugestão para extrair dados).

## A API: PokéAPI

Usaremos o seguinte *endpoint* para buscar um Pokémon:
`https://pokeapi.co/api/v2/pokemon/{nome_ou_id}`

- Substitua `{nome_ou_id}` pelo nome (em minúsculas, ex: `pikachu`) ou pelo ID do Pokémon (ex: `25`).

**Exemplo de Resposta JSON (simplificada):**
```json
{
  "id": 25,
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "types": [
    {
      "type": { "name": "electric" }
    }
  ],
  "abilities": [
    {
      "ability": { "name": "static" }
    },
    {
      "ability": { "name": "lightning-rod" }
    }
  ]
}
```

## Requisitos

Você deve criar as classes e a lógica para consumir a API e popular sua Pokédex.

### 1. Módulo de API (`pokedexbuilder/api.py` )
Crie um novo arquivo `api.py` dentro de `pokedexbuilder`.
- **Função `buscar_pokemon(nome_ou_id)`:**
    - Recebe o nome ou ID de um Pokémon.
    - Constrói a URL da API.
    - Usa `requests.get()` para fazer a chamada.
    - Verifica se a resposta foi bem-sucedida (status code 200).
    - Se sim, retorna o conteúdo JSON (`response.json()`).
    - Se não, imprime uma mensagem de erro e retorna `None`.

### 2. Classes de Modelo (`pokedexbuilder/models.py`)

#### a. Classe `Pokemon`
- **Atributos:**
    - `id` (int)
    - `nome` (str)
    - `altura` (int)
    - `peso` (int)
    - `tipos` (list de strings): Ex: `['electric']`
    - `habilidades` (list de strings): Ex: `['static', 'lightning-rod']`
- **Método `__init__`:**
    - O construtor deve receber o JSON de um Pokémon como argumento.
    - Dentro do `__init__`, você deve extrair os valores do JSON e atribuí-los aos atributos da classe.
    - **Dica:** Para `tipos` e `habilidades`, você precisará iterar sobre as listas no JSON. Uma *list comprehension* é perfeita para isso!

#### b. Classe `Pokedex`
- **Atributos:**
    - `dono` (str): Nome do dono da Pokédex.
    - `pokemons` (dict): Um dicionário para armazenar os Pokémon capturados. A chave pode ser o `id` e o valor o objeto `Pokemon`.
- **Métodos:**
    - `adicionar_pokemon(self, pokemon)`: Adiciona uma instância de `Pokemon` ao dicionário `pokemons`.
    - `listar_pokemons(self)`: Imprime no console um resumo de cada Pokémon na Pokédex.

## Passo a Passo Sugerido

1.  **Crie a função de API:** Implemente a função `buscar_pokemon` para se comunicar com a PokéAPI.
2.  **Defina as Classes:** Vá para `pokedexbuilder/models.py` e crie as classes `Pokemon` e `Pokedex`. Preste atenção especial ao `__init__` da classe `Pokemon`, que fará o "parse" do JSON, use `import json` ou `from json import loads`.
3.  **Junte Tudo no `main.py`:**
    a. Importe suas classes e a função da API.
    b. Crie uma instância da `Pokedex`.
    c. Peça ao usuário para digitar o nome de um Pokémon.
    d. Chame `buscar_pokemon` com a entrada do usuário.
    e. Se a busca for bem-sucedida, crie um objeto `Pokemon` com os dados e adicione-o à Pokédex.
    f. No final, liste os Pokémon capturados.

## Desafio Extra (Opcional)

Adicione um método à classe `Pokedex` chamado `buscar_por_tipo(self, tipo)`. Este método deve retornar uma lista de todos os objetos `Pokemon` na sua Pokédex que pertencem ao `tipo` especificado (ex: "fire", "water").

class Pokemon:
    """
    Representa um Pokémon com dados extraídos da PokéAPI.

    Atributos:
        `id` (int): O número do Pokémon na Pokédex nacional.
        `nome` (str): O nome do Pokémon.
        `altura` (int): A altura do Pokémon em decímetros.
        `peso` (int): O peso do Pokémon em hectogramas.
        `tipos` (list): Uma lista de strings com os tipos do Pokémon.
        `habilidades` (list): Uma lista de strings com as habilidades do Pokémon.
    """
    def __init__(self, dados_json: dict):
        '''
        TODO
        ----

        Extraia os dados do dicionário `dados_json` e atribua-os aos atributos da classe.
        '''
        self.id = dados_json['id']
        self.nome = dados_json['name']
        self.altura = dados_json['height']
        self.peso = dados_json['weight']

        # List comprehension para tipos
        self.tipos = [item['type']['name'] for item in dados_json['types']]

        # List comprehension para habilidades
        self.habilidades = [
            item['ability']['name'] for item in dados_json['abilities']
        ]

    def __str__(self):
        return f"#{self.id:03d} - {self.nome.capitalize()}"


class Pokedex:
    """
    Representa uma Pokédex que armazena os Pokémon capturados.

    Atributos:
        `dono` (str): O nome do treinador que possui a Pokédex.
        `pokemons` (dict): Um dicionário de Pokémon, onde a chave é o ID
                         e o valor é o objeto Pokemon.
    """

    def __init__(self, dono):
        '''
        TODO
        ----
        Inicialize os atributos 'dono' e 'pokemons' (como um dicionário vazio).
        '''
        self.dono = dono
        self.pokemons = {}  # id → Pokemon

    def adicionar_pokemon(self, pokemon):
        """
        TODO
        ----
        Adiciona um objeto Pokemon ao dicionário da Pokédex.
        A chave deve ser o ID do pokemon.
        """
        self.pokemons[pokemon.id] = pokemon

    def listar_pokemons(self):
        """
        TODO
        ----
        Itere sobre o dicionário `'self.pokemons'` e imprima os detalhes de cada um.
        """
        print(f"Pokédex de {self.dono}:")
        if not self.pokemons:
            print("  Nenhum Pokémon capturado ainda.")
            return
        
        for pokemon in self.pokemons.values():
            print(f"  {pokemon} | Tipos: {pokemon.tipos}")

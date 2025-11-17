from pokedexbuilder.api import buscar_pokemon
from pokedexbuilder.models import Pokemon, Pokedex

def main():
    print("=== Bem-vindo ao Construtor de Pokédex ===")
    nome_treinador = input("Digite o nome do treinador: ")

    pokedex = Pokedex(nome_treinador)

    while True:
        entrada = input("\nDigite o nome ou ID de um Pokémon (ou 'sair'): ")

        if entrada.lower() == "sair":
            break

        dados = buscar_pokemon(entrada)

        if dados:
            pokemon = Pokemon(dados)
            pokedex.adicionar_pokemon(pokemon)
            print(f"✓ {pokemon.nome.capitalize()} adicionado à Pokédex!")
        else:
            print("Nenhum Pokémon foi adicionado.")

    print("\n=== Pokémons Capturados ===")
    pokedex.listar_pokemons()


if __name__ == "__main__":
    main()

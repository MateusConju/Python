import requests

def buscar_pokemon(nome_ou_id):
    """
    Faz uma requisição à PokéAPI para buscar um Pokémon pelo nome ou ID.

    Retorna o JSON (dict) se encontrado, ou None se houver erro.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_ou_id.lower()}"
    print(f"Buscando dados em: {url}")

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print("Erro: Pokémon não encontrado!")
            return None

    except requests.RequestException:
        print("Erro ao se conectar à API.")
        return None

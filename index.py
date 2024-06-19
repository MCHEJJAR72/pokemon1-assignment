Step 1: Fetch Data from PokeAPI
We'll define functions to fetch Pokémon data from the API and organize them by type.
python
Copy code
import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to fetch data for {pokemon_name}")
        return None

def fetch_pokemon_info(pokemon_name):
    pokemon_data = fetch_pokemon_data(pokemon_name)
    if pokemon_data:
        abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
        weight = pokemon_data['weight']
        types = [type['type']['name'] for type in pokemon_data['types']]
        return {
            'abilities': abilities,
            'weight': weight,
            'types': types
        }
    else:
        return None
Step 2: Organize Pokémon by Type
Now, we'll create a dictionary to categorize Pokémon by their types:
python
Copy code
def categorize_pokemon(pokemon_list):
    categorized_pokemon = {}

    for pokemon_name in pokemon_list:
        pokemon_info = fetch_pokemon_info(pokemon_name)
        if pokemon_info:
            types = pokemon_info['types']
            for type_name in types:
                if type_name not in categorized_pokemon:
                    categorized_pokemon[type_name] = {}
                categorized_pokemon[type_name][pokemon_name] = {
                    'abilities': pokemon_info['abilities'],
                    'weight': pokemon_info['weight']
                }
    
    return categorized_pokemon
Step 3: Example Usage
Finally, let's fetch data for 20 Pokémon and categorize them by type:
python
Copy code
pokemon_list = [
    'bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon',
    'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie',
    'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey',
    'pidgeotto', 'pidgeot', 'rattata', 'raticate'
]

categorized_pokemon = categorize_pokemon(pokemon_list)

# Print the categorized_pokemon dictionary
for type_name, pokemons in categorized_pokemon.items():
    print(f"{type_name}:")
    for pokemon_name, info in pokemons.items():
        abilities = ', '.join(info['abilities'])
        weight = info['weight']
        print(f"\t{pokemon_name}:")
        print(f"\t\tAbilities: {abilities}")
        print(f"\t\tWeight: {weight}")

from pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        pokemon_names = [pokemon.name for pokemon in self.pokemons]
        if pokemon_name not in pokemon_names:
            return f"Pokemon is not caught"

        pokemon_to_remove_index = pokemon_names.index(pokemon_name)
        self.pokemons.pop(pokemon_to_remove_index)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        data = ""
        data += f"Pokemon Trainer {self.name}\n"
        data += f"Pokemon count {len(self.pokemons)}"

        for pokemon in self.pokemons:
            data += f"\n- {pokemon.pokemon_details()}"

        return data


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
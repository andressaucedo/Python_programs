# practice_poke - an illustration of how objects work

def pokemon():
    import random

    class Pokemon:  # Here we are declaring the class name.
        def __init__(self,name,energy_type,hp,weakness):  
            self.name = name
            self.energy_type = energy_type
            self.hp = hp
            self.weakness = weakness

          
    charmander = Pokemon('Charmander','fire',3800,'water')
    bulbasaur = Pokemon('Bulbasaur','grass',3200,'fire')
    meowth = Pokemon('Meowth','psychic',2800,'fighting')
    
    pokedex = [charmander,bulbasaur,meowth]

    print(f"variable pokedex is type: {type(pokedex)}")
    print("pokedex contains:")
    for i in pokedex:
        print(i.name)
    print("\ncharmanders stats:")
    print(f"\t{charmander.name}\n\t{charmander.energy_type}\n\t{charmander.hp}\n\t{charmander.weakness}\n")

    random_pokemon  = random.choice(pokedex)
    print(f"Let's pick a random pokemon! I choose you {random_pokemon.name}!\n")
    
    
if __name__ == "__main__":
    pokemon()
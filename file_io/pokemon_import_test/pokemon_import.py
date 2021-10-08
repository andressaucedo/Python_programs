# pokemon_import.py - test program to import a master list and create a party
# which gets exported to a json file. 

def pokemon_importer(file_path):
    import json

    # Declaring the Pokemon object class and attributes
    class Pokemon:
        def __init__(self, name, types, hp, attacks, weaknesses):
            self.name = name
            self.types = types
            self.hp = hp
            self.attacks = attacks
            self.weaknesses = weaknesses    

    # Opening data file in the function call argument
    datafile = open(file_path,)

    if file_path == None:
        print("Invalid path argument")
        print(f"Usage: {__name__} [ JSON file path]\n")
        return 1
    # Create dict from json file
    master_dict = json.load(datafile)
    while(1):
        # Prompt the user for a pokemon name.
        print("'quit' to end")
        pokemon_name = input("Enter a pokemon name: ")
        if pokemon_name == 'quit':
            outfile.close()
            break
        found = 0
        # Search the imported file as dict for the given name of pokemon.
        for i in master_dict:
            # If found, pokemon assigned to object, found flag set to 1.
            if i['name'].lower() == pokemon_name.lower():
                found = 1
                buddy = Pokemon(
                    i['name'],
                    i['types'],
                    i['hp'],
                    i['attacks'],
                    i['weaknesses'])           
        
        if found != 1:
            print("Your entry was not found")
        # Print out the object attributes from found pokemon 
        else:    
            print (f"\tName: {buddy.name}")
            for i in buddy.types:
                print (f"\tType: {i}")
            print (f"\tHP: {buddy.hp}")
            for i in buddy.attacks:
                print (f"\tAttack: {i['name']} - Damage: {i['damage']}")
            print (f"\tWeakness: {buddy.weaknesses[0]['type']} - Multiplier: {buddy.    weaknesses[0]['value']}")

        # Option to add pokemon to output file 'myparty.json'
        choice = input("Add to Party?: ")
        if choice[0].lower() == 'y':
            bd = vars(buddy)
            with open('myparty.json','a') as outfile:
                json.dump(bd,outfile)

    
if __name__ == "__main__":
        pokemon_importer('my_pokemon_master_list.json')
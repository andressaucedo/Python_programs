def pokemon_importer(file_path):
    import json

    class Pokemon:
        def __init__(self, name, types, hp, attacks, weaknesses):
            self.name = name
            self.types = types
            self.hp = hp
            self.attacks = attacks
            self.weaknesses = weaknesses    

    datafile = open(file_path,)

    if file_path == None:
        print("Invalid path argument")
        print(f"Usage: {__name__} [ JSON file path]\n")
        return 1

    master_dict = json.load(datafile)
    while(1):
        pokemon_name = input("Enter a pokemon name: ")

        found = 0
        for i in master_dict:
            if i['name'] == pokemon_name:
                found = 1
                buddy = Pokemon(
                    i['name'],
                    i['types'],
                    i['hp'],
                    i['attacks'],
                    i['weaknesses'])           
        
        if found != 1:
            print("Your entry was not found")
        
       
            
        print (f"\tName: {buddy.name}")
        for i in buddy.types:
            print (f"\tType: {i}")
        print (f"\tHP: {buddy.hp}")
        for i in buddy.attacks:
            print (f"\tAttack: {i['name']} - Damage: {i['damage']}")
        print (f"\tWeakness: {buddy.weaknesses[0]['type']} - Multiplier: {buddy.weaknesses[0]['value']}")
        

        choice = input("Search another?")
        if choice[0] == 'y' or choice[0] == 'Y':
            continue
        else:
            return 0

if __name__ == "__main__":
    pokemon_importer('my_pokemon_master_list.json')



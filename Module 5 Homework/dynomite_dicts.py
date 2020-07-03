if __name__ == '__main__':
    pokedex = {}

    pokedex.update({
        'Venosaur': ['Grass', 'Poison'],
        'Charizard': ['Fire', 'Flying'],
        'Blastoise': ['Water']
        })

    del pokedex['Blastoise']

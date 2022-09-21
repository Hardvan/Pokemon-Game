import PythonGrammar,PokemonMechanisms

def choice():
    
    print('Do you want to go to the Pokemon Center?')
    while True:
        choice = input('Enter [Y/N]: ')
        choice = choice.upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print('Enter \'Y\' or \'N\' only.')
            continue
    
    return


def displayPokemonCenterBriefing(user_details):
        
    print('Nurse Joy:','Hi there, this is the infamous Pokemon Center!')
    print('Nurse Joy:','There are rumours floating around that we secretly traffic Pokemons. Of course it is just a rumour, right?!')
    print('Nurse Joy:','\'Evil Menacing Laugh\'')
    print('Nurse Joy:','How can I be of service?')
    PythonGrammar.Loading(user_details['Name']+'gives Pokemon')
    
    return


def use(user_details):
    
    user_pokemon = user_details['Starter Pokemon']
    
    displayPokemonCenterBriefing(user_details)
    
    if user_pokemon['HP'] < 0:
        print('Nurse Joy:','Oh no! It looks like your',user_pokemon['Name'],'has fainted.')
        print('Nurse Joy:','Not to worry, you have come to the right place!')
        PythonGrammar.TimePause()
    else:
        pass
    
    PokemonMechanisms.FullHeal(user_pokemon)
    
    PokemonMechanisms.RefreshAttackCounters(user_pokemon)
    
    print('Nurse Joy:','Come back soon dear!')
    print('Nurse Joy:','And next time, bring even more exotic Pokemons!!!')
    print(user_details['Name'],'rushed off hurriedly')
    
    return
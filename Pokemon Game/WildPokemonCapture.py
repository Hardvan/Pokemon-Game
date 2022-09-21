import PythonGrammar

def Choice(wild_pokemon):
    
    print('Do you want to capture the Wild',wild_pokemon['Name'],'?')
    while True:
        choice = input('Enter [Y/N] to CAPTURE or NOT CAPTURE: ')
        choice = choice.upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print('Enter either \'Y\' or \'N\' only')
            continue
    
    return

def CaptureMain(user_details,wild_pokemon):
    
    capture = False
    
    #No. of Pokeballs
    pokeballs = user_details['Pokeballs']
    
    while True:
        
        #Exiting Loop if No Pokeballs Left
        if pokeballs <= 0:
            print('Oh no! It looks like you have run out of Poke-Balls!')
            break
        else:
            pass
        
        capture = chance(wild_pokemon)
        
        #Displaying Capture Process
        displayCapture(capture)
        
        #Displaying Number of Pokeballs Left
        pokeballs -= 1
        print('No. of pokeballs left:',pokeballs)
        PythonGrammar.TimePause()
        
        #Exiting Loop if SUCCESSFULL CAPTURE
        if capture == True:
            break
        else:
            pass
        
        #Try Again or Exit
        if CaptureAgain() == True:
            PythonGrammar.displayBlankLine()
            print('Trying to catch the Pokemon again!')
            continue
        else:
            break
    
    #Updating Pokeballs in User Dictionary
    user_details['Pokeballs'] = pokeballs
    
    if capture == True:
        GiveWildPokemon(user_details,wild_pokemon)
    else:
        PythonGrammar.displayBlankLine()
        print('Bad Luck! The Wild',wild_pokemon['Name'],'has escaped the Capture.')
        PythonGrammar.displayBlankLine()
        PythonGrammar.displayLine()
        PythonGrammar.displayBlankLine()
    
    return capture
            
def chance(wild_pokemon):
    
    import random
    
    capture=False
    
    #Percentage of HP80
    HP_percentage = (wild_pokemon['HP']/wild_pokemon['Max HP']) * 100
    HP_percentage = round(HP_percentage,2)
    
    #Displaying Wild Pokemon HP %
    PythonGrammar.displayBlankLine()
    print('Wild',wild_pokemon['Name'],'\'s HP % is =',HP_percentage)
    
    #Calculating CHANCE
    
    #10% chance if HP > 90%
    if HP_percentage > 90:
        if 7 == random.randint(1,10):
            capture = True
        
    #40% chance if HP > 50%
    elif HP_percentage > 50:
        n = random.randint(1,5)
        if n in [2,3]:
            capture = True
        
    #80% chance if HP > 10%
    elif HP_percentage > 10:
        n = random.randint(1,5)
        if n in [1,2,3,4]:
            capture = True
        
    #90% chance if HP > 0%
    else:
        n = random.randint(1,10)
        if n in [1,2,3,4,5,6,7,8,9]:
            capture = True
    
    return capture
         
def displayCapture(capture):
    
    PythonGrammar.Loading('Capturing')
    if capture == True:
        print('The Capture was SUCCESSFULL!')
    else:
        print('The Pokemon ESCAPED The Capture.')
    
    PythonGrammar.displayBlankLine()
    PythonGrammar.TimePause()
    
    return

def CaptureAgain():
    
    choice = False
    
    PythonGrammar.displayBlankLine()
    print('Do you want to try to Capture the Pokemon Again?')
    while True:
        choice=input('Enter \'Y\' for YES or \'N\' for NO: ')
        choice=choice.upper()
        if choice == 'Y':
            choice = True
            break
        elif choice == 'N':
            choice = False
            break
        else:
            print('Enter either \'Y\' or \'N\' only.')
            continue
    
    PythonGrammar.displayLine()
    
    return choice

def GiveWildPokemon(user_details,wild_pokemon):
    
    #Adding Pokemon to User's Captured Pokemons
    user_details['Captured Pokemons']={}
    user_details['Captured Pokemons'][1] = wild_pokemon
    
    #Displaying
    PythonGrammar.Loading('Giving Wild Pokemon')
    
    print(user_details)
    PythonGrammar.TimePause()
    PythonGrammar.displayLine()
    
    return
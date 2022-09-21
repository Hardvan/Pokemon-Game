import ReadyConfirmExits,PythonGrammar

def Nickname():
    
    #Getting Nickname
    while True:
        nickname = input('Enter your username or if you are cooler then enter your nickname: ')
        
        #Confirming Choice
        exits = ReadyConfirmExits.Confirm()
        if exits == True:
            break
        elif exits == False:
            continue

    #Out Of Loop
    PythonGrammar.displayBlankLine()
    print('FRIENDLY AI: That\'s a nice name! (is what I have been programmed to say)')
    PythonGrammar.TimePause()
    PythonGrammar.displayLine()
    
    return nickname


def displayStarterPokemonTable():
    
    print('+---------------+------------+')
    print('|','   Pokemon','\t\t|\t','Type','     |',sep='')
    print('+---------------+------------+')
    print('|','1. Charmander','\t|\t','Fire','     |',sep='')
    print('|','2. Squirtle','\t|\t','Water','    |',sep='')
    print('|','3. Bulbasaur','\t|\t','Grass','    |',sep='')
    print('+---------------+------------+')
    PythonGrammar.displayBlankLine()
    
    return
 
   
def StarterPokemon():
    
    #Choosing Starter Pokemon
    starter_pokemon = {} #Dicitonary containing Name, Type, HP of Pokemon
    Name = Type = HP = None
    
    PythonGrammar.displayBlankLine()
    print('FRIENDLY AI: Choose your starter Pokemon!')
    PythonGrammar.displayBlankLine()
    
    PythonGrammar.TimePause()
    
    PythonGrammar.Loading('Choose Wisely')
    
    while True:
        
        displayStarterPokemonTable()
        choice = input('Enter your choice(1-3): ')
        PythonGrammar.displayBlankLine()
        
        if choice in ['1','2','3']:
            choice=int(choice)
            
            #CHARMANDER
            if choice == 1:
                Name = 'Charmander'
                Type = 'Fire'
                HP = 80
                evolve2 = 'Charmeleon'
                evolve3 = 'Charizard'
                print('FRIENDLY AI: Playing with fire I see!')
            
            #SQUIRTLE
            elif choice == 2:
                Name = 'Squirtle'
                Type = 'Water'
                HP = 80
                evolve2 = 'Wartortle'
                evolve3 = 'Blastoise'
                print('FRIENDLY AI: Water down your opponents with that!')
            
            #BULBASAUR
            elif choice == 3:
                Name = 'Bulbasaur'
                Type = 'Grass'
                HP = 80
                evolve2 = 'Ivysaur'
                evolve3 = 'Venusaur'
                print('FRIENDLY AI: Bulbasaur? More like Buddy-saur!')
            
            PythonGrammar.displayBlankLine()
            print('Your choice:',Name)
            PythonGrammar.displayBlankLine()
            print('Are you sure with your choice?')
                
            #Confirming Choice
            exits = ReadyConfirmExits.Confirm()
                
            if exits == False:
                continue
            elif exits == True:
                break
                
        else: #Not in [1,2,3]
            print('Enter a numer in the range (1-3) only.')
            PythonGrammar.TimePause()
            PythonGrammar.Loading('Displaying Again')
            PythonGrammar.displayBlankLine()
            continue
    
    XP = 0
    max_XP = 100
    level = 1
    
    starter_pokemon['Name'] = Name
    starter_pokemon['Type'] = Type
    starter_pokemon['HP'] = HP
    starter_pokemon['Max HP'] = HP
    starter_pokemon['XP'] = XP
    starter_pokemon['Max XP'] = max_XP
    starter_pokemon['Level'] = level
    starter_pokemon['2nd Form'] = evolve2
    starter_pokemon['3rd Form'] = evolve3
    starter_pokemon['Current Form'] = 1
    
    return starter_pokemon
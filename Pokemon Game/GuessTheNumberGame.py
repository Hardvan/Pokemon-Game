import PythonGrammar
import random

def Ready():
    
    PythonGrammar.displayBlankLine()
    print('Are you ready for the adventure that awaits you?!')
    while True:
        ready=input('Enter Y/y to continue: ')
        ready=ready.upper()
        if ready=='Y':
            PythonGrammar.Loading('Continuing')
            break
        else:
            PythonGrammar.Loading('Waiting for you to proceed')
            continue
    return


def GuessTheNumberBriefing():
    
    PythonGrammar.displayBlankLine()
    print('Hello, hello, hello!')
    PythonGrammar.displayBlankLine()
    print('Do you want to heal your Pokemon? Well, then you have come to the right place!')
    print('You will have to play a mini-game in order to revitalise your Pokemon!')
    PythonGrammar.displayBlankLine()
    PythonGrammar.TimePause()
    print('The mini-game\'s called GUESS THE NUMBER!')
    PythonGrammar.displayBlankLine()
    print('You will be given 3 Chances to accurately guess a number hand-picked by the AI.')
    print('The number will be in the range 1 - 10, both inclusive.')
    PythonGrammar.displayBlankLine()
    print('If you win in','\t\t','Your Score',sep='')
    print('1st Try','\t\t\t\t',100,sep='')
    print('2nd Try','\t\t\t\t',80,sep='')
    print('3rd Try','\t\t\t\t',60,sep='')
    PythonGrammar.displayBlankLine()
    PythonGrammar.TimePause()
    print('Your Pokemon will be healed according to the score you get.')
    PythonGrammar.TimePause()
    
    return


def GetCompNumber():
    
    n = random.randint(1,10)
    return n


def GetUserNumber():
    
    while True:
        
        user_number=input('Enter your guess: ')
        if user_number.isnumeric():
            user_number=int(user_number)
            if user_number in range(1,11): #1 to 10
                break
            else:
                print('Enter a number in the range 1 - 10 only')
                continue
        else:
            print('Enter a number in the range 1 - 10 only')
            continue
        
    PythonGrammar.displayBlankLine()
    
    return user_number


def displayCurrentScore(score):
    
    print('Your Current Score:',score)
    PythonGrammar.displayBlankLine()
    PythonGrammar.displayLine()
    PythonGrammar.TimePause()
    
    return


def play():
    
    #Displaying Details of the Mini-Game
    GuessTheNumberBriefing()
    
    Ready()
    
    #GAME STARTS
    
    #Getting Computer Number
    comp_number = GetCompNumber()
    
    #Game Variables
    win = False
    count = 0
    score = 100
    
    #Loop ends when either 3 Guesses are over or User wins before 3 guesses
    while True:
        
        #Updating no. of guesses
        count += 1
        PythonGrammar.displayBlankLine()
        
        #Exiting the loop if 3 guesses are done
        if count > 3:
            score = 60
            print('3 Guesses are over!')
            break
        else:
            print('No. Of Guesses:',count,'of 3')
        
        #Getting User Number
        user_number = GetUserNumber()
        win, score = CheckNumberAndUpdateScore(user_number,comp_number,count,score)
        
        #Displaying Current Score
        displayCurrentScore(score)
        
        if win==True:
            break
        else:
            continue
    
    #OUT OF LOOP
    PythonGrammar.displayBlankLine()
    print('Your Final Score:',score)
    PythonGrammar.TimePause()
    
    PythonGrammar.displayBlankLine()
    PythonGrammar.displayLine()
    
    return win,score
                
def CheckNumberAndUpdateScore(user_number,comp_number,count,score):
    
    win = False
    
    #If both number match
    if user_number == comp_number:
        
        win = True
        print('+------------------------+')
        print('|It\'s the correct number!|')
        print('+------------------------+')
    
    elif user_number > comp_number or user_number < comp_number:
        
        print('It\'s incorrect!')
        PythonGrammar.displayBlankLine()
        
        score -= 20
        if score < 60:
            score == 60
        
        if count == 1: #1st HINT
            
            if comp_number > 5:
                print('The number is in the upper half of 1-10')
            else:
                print('The number is in the lower half of 1-10')
        
        if count == 2: #2nd HINT
            
            if comp_number in [4,5,6]:
                print('The number is somewhere near the middle.')
            else:
                print('The number is near the extreme ends.')
        
        if user_number > comp_number: #COMPULSORY HINT
            print('The number is lesser than',user_number)
        else:
            print('The number is greater than',user_number)
    
    PythonGrammar.displayBlankLine()
    PythonGrammar.TimePause()
    
    return win,score


def displayHealPokemon(user_details,old_hp,new_hp,health_add):
    
    user_name = user_details['Name']
    user_pokemon = user_details['Starter Pokemon']
    
    PythonGrammar.displayBlankLine()
    print('HP of',user_name,'\'s',user_pokemon['Name'],'is:',old_hp)
    PythonGrammar.TimePause()
    
    PythonGrammar.Loading('Getting Medical Supplies')
    
    #Displaying New HP
    print('We healed',health_add,'HP.')
    print('HP of',user_name,'\'s',user_pokemon['Name'],'after performing extreme medical procedures is:',new_hp)
    PythonGrammar.TimePause()
    PythonGrammar.displayLine()
    
    return


def PlayAgain(user_details):
    
    PythonGrammar.displayBlankLine()
    print('Do you want to try the mini-game again?')
    while True:
        choice=input('Enter Y for \'YES\' or N for \'NO\': ')
        choice=choice.upper()
        if choice=='Y':
            return True
        elif choice=='N':
            return False
        else:
            print('Enter [Y/N] only.')
            continue
    
    return


def HealPokemon(user_details,score):
    
    import random
    
    user_pokemon = user_details['Starter Pokemon']
    
    old_hp = user_pokemon['HP']
    
    #Adding HP
    health_add = score * random.uniform(0.1,0.3) #RANGE: 6 to 30
    health_add *= random.uniform(1,1.2) #x1 to x1.2
    health_add += HealthAddRandomiser(user_pokemon)
    health_add = round(health_add)
    user_pokemon['HP'] += health_add
    
    #In case HP crosses upper limit of 80
    if user_pokemon['HP'] > user_pokemon['Max HP']:
        user_pokemon['HP'] = user_pokemon['Max HP']
    
    new_hp = user_pokemon['HP']
    
    #Displaying New HP
    displayHealPokemon(user_details,old_hp,new_hp,health_add)
    
    return


def HealthAddRandomiser(user_pokemon):
    
    hp = user_pokemon['HP']
    x = (10/100) * hp
    x += random.randint(x,x+7) + random.randint(x-3,x+4) - random.randint(x-2,x) - random.randint(x-7,x-3)
    return x
    
    
    
    
    
    
    
    
    
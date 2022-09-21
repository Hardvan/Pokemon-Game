import PythonGrammar
import ReadyConfirmExits

def Choice(villager_details):
    
    #Last line before this was 'I will reward you with: HP Potion'
    
    print('Accept',villager_details['Name']+'\'s Challenge?')
    PythonGrammar.displayBlankLine()
    
    while True:
        choice = input('Enter [Y/N]: ')
        choice = choice.upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print('Enter either \'Y\' or \'N\' only.')
            continue
    
    return


def getCompChoice():
            
    import random
    compchoice = random.randint(1,3) 
    if compchoice == 1:
        compchoice = 'Rock'
    elif compchoice == 2:
        compchoice = 'Paper'
    elif compchoice == 3:
        compchoice = 'Scissors'
    
    return compchoice


def getUserWeaponChoice():
    
    userchoice = None
    print('\nChoose your WEAPON:')
    print('\n1. Rock (R)')
    print('2. Paper (P)')
    print('3. Scissors (S)')
    
    while True:   #Getting User's Choice
    
        userchoice=input('Choose (R,P,S)/(Rock,Paper,Scissors) or (1,2,3): ')
        PythonGrammar.displayBlankLine()
        
        if userchoice.isnumeric():                 #User Enters A Number
        
            userchoice = int(userchoice)
            if userchoice not in [1,2,3]:
                print('Enter a Valid Option.')
                continue
            else:
                if userchoice == 1:
                    userchoice = 'Rock'
                elif userchoice == 2:
                    userchoice = 'Paper'
                elif userchoice == 3:
                    userchoice = 'Scissors'
                    
                break
        
        elif userchoice.isalpha():       #User Enters Letters
        
            userchoice = userchoice.upper()
            if userchoice not in ['ROCK','PAPER','SCISSORS'] and userchoice not in ['R','P','S']:
                print('Enter A Valid Option.')
                continue
            elif userchoice in ['ROCK','PAPER','SCISSORS'] or userchoice in ['R','P','S']:
                if userchoice[0] == 'R':
                    userchoice = 'Rock'
                elif userchoice[0] == 'P':
                    userchoice = 'Paper'
                elif userchoice[0] == 'S':
                    userchoice = 'Scissors'
                        
                break
            else:
                print('Enter A Valid Option.')
                continue
        
        else:                                      #User Enters Wrong Option
            print('Enter A Valid Option.')
            continue
            
    return userchoice
        

def displayMovesPlayed(userchoice,compchoice):
    
    print('You play the move: ',end='')
    PythonGrammar.TimePause()
    print(userchoice)
    print('AI plays the move: ',end='')
    PythonGrammar.TimePause()
    print(compchoice)
    
    return
        

def calculateOutcome(userchoice,compchoice,userwins,compwins,tie):
    
    PythonGrammar.Loading('Calculating')
    
    if userchoice[0]=='R' and compchoice[0]=='P': #USER=ROCK and COMP=PAPER
        compwins+=1
        print('Paper BEATS Rock!')
        print('')
        print('The AI has won this round.')
    elif userchoice[0]=='R' and compchoice[0]=='S': #USER=ROCK and COMP=SCISSORS
        userwins+=1
        print('Rock BEATS Scissors!')
        print('')
        print('The Human has won this round.')
    elif userchoice[0]=='R' and compchoice[0]=='R': #USER=ROCK and COMP=ROCK
        tie+=1
        print('Rock and Rock and ROLL! It\'s a tie.')
        print('')
        print('The Human and AI are on equal footing, for now...')

    elif userchoice[0]=='P' and compchoice[0]=='S': #USER=PAPER and COMP=SCISSORS
        compwins+=1
        print('Scissors TEAR Paper!')
        print('')
        print('The AI has won this round.')
    elif userchoice[0]=='P' and compchoice[0]=='R': #USER=PAPER and COMP=ROCK
        userwins+=1
        print('Paper BEATS Rock!')
        print('')
        print('The Human has won this round.')
    elif userchoice[0]=='P' and compchoice[0]=='P': #USER=PAPER and COMP=PAPER
        tie+=1
        print('Paper and Paper, not very PROPER! It\'s a tie.')
        print('')
        print('The Human and AI are on equal footing, for now...')

    elif userchoice[0]=='S' and compchoice[0]=='R': #USER=SCISSORS and COMP=ROCK
        compwins+=1
        print('Rock BEATS Scissors!')
        print('')
        print('The AI has won this round.')
    elif userchoice[0]=='S' and compchoice[0]=='P': #USER=SCISSORS and COMP=PAPER
        userwins+=1
        print('Scissors TEARS Paper!')
        print('')
        print('The Human has won this round.')
    elif userchoice[0]=='S' and compchoice[0]=='S': #USER=SCISSORS and COMP=SCISSORS
        tie+=1
        print('Scissors and Scissors, not a nice PAIR! It\'s a tie.')
        print('')
        print('The Human and AI are on equal footing, for now...')
            
    return userwins,compwins,tie


def displayScoreAndRound(user_details,villager_details,userwins,compwins,tie,roundno,n):
    
    PythonGrammar.Loading('Fetching Results')
    PythonGrammar.TimePause()
    print('CURRENT SCORE:')
    PythonGrammar.displayBlankLine()
    PythonGrammar.TimePause()
    print(user_details['Name'],'WINS:',userwins)
    print(villager_details['Name'],'WINS:',compwins)
    print(user_details['Name'],'AND',villager_details['Name'],'TIES:',tie)
    print('No. Of Rounds Done:',roundno,'/',n)
    PythonGrammar.TimePause()
    
    return


def ProceedNextRound(villager_details,roundno):
            
    PythonGrammar.displayBlankLine()
    print('Proceed to next round?')
    PythonGrammar.displayBlankLine()
    
    exits = ReadyConfirmExits.Exits()
    
    if roundno == 3: #For Last Round
        exits = True
    
    return exits
        
def checkUserWin(userwins,compwins,tie):
    
    win = None
    
    if userwins > compwins:
        print('You have won!')
        win = True
    else:
        print('You have lost. Better luck next time!')
        win = False

    return win


def displayFinalResult(user_details,villager_details,userwins,compwins,tie):
    
    PythonGrammar.displayBlankLine()
    print('Total No. of times',user_details['Name'],'won:',userwins)
    print('Total No. of times',villager_details['Name'],'won:',compwins)
    print('Total No. of times it was a tie:',tie)
    
    return


def play(user_details,villager_details):

    #Score
    userwins = compwins = tie = 0
    
    #No. Of Rounds
    n = 3
    
    for roundno in range(1,n+1):
        
        #Computer Choosing Rock, Paper or Scissors
        compchoice = getCompChoice()
        
        #User Choosing Weapon
        userchoice = getUserWeaponChoice()
    
        #DISPLAYING USER'S AND AI'S MOVES
        displayMovesPlayed(userchoice,compchoice)
        
        #CALCULATING WHO WON
        userwins,compwins,tie = calculateOutcome(userchoice,compchoice,userwins, compwins, tie)
        
        #DISPLAYING CURRENT SCORE AND ROUND NO.
        displayScoreAndRound(user_details,villager_details,userwins,compwins,tie,roundno,n)
        
        #Proceed or Exit
        exits = ProceedNextRound(villager_details,roundno)
        
        if exits == True: #Exiting Loop if User wants to Quit
            PythonGrammar.Loading('Escaping from '+villager_details['Name'])
            PythonGrammar.displayLine()
            break
        else:
            PythonGrammar.Loading('Continuing the Long Battle')
            PythonGrammar.displayLine()
            continue
                
                    
    
    #OUTSIDE THE LOOP
    displayFinalResult(user_details, villager_details, userwins, compwins, tie)
    
    win = checkUserWin(userwins,compwins,tie)
    
    return win


def playagain(user_details):
    
    PythonGrammar.displayBlankLine()
    print('Do you want to try the mini-game again?')
    while True:
        choice = input('Enter \'Y\' for yes or \'N\' for no: ')
        choice = choice.upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print('Enter [Y/N] only.')
            continue
    
    return
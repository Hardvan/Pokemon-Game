import PythonGrammar

def Exits():
    
    exits = False
    
    print('Enter any key to CONTINUE')
    print('\t\tOR')
    print('Enter E/e to ESCAPE from Battle')
    key=input('Enter: ')
    if key in ['e','E']:
        exits=True
    else:
        exits=False
    
    return exits


def Confirm():

    #Confirming Choice and Returning True or False
    exits=True
    
    while True:
        confirm=input('Press Y/y to CONFIRM or N/n to CHANGE: ')
        confirm=confirm.upper()
        if confirm=='Y':
            exits==True
            PythonGrammar.Loading('Confirming')
            break
                    
        elif confirm=='N':
            exits=False
            PythonGrammar.Loading('Prompting Again')
            break
                    
        else:
            print('Enter either Y or N only.')
            continue
    #Choice Confirmed
    
    return exits


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

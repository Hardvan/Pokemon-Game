import PythonGrammar

def giveItem(user_details, villager_details):
    
    #Giving the Villager's Item to User
    user_details['Items']={}
    user_details['Items'][1]={}
    user_details['Items'][1]['Name'] = villager_details['Item']
    user_details['Items'][1]['Status'] = 'Not Used'
    
    print(villager_details['Name'],'has given you',villager_details['Item'])
    PythonGrammar.displayBlankLine()
    print(villager_details['Item'],'Equipped in the Backpack.')
    PythonGrammar.displayBlankLine
    PythonGrammar.displayLine()
    PythonGrammar.displayBlankLine()
    PythonGrammar.TimePause()
    
    return


def useItem(user_details):
    
    item = user_details['Items'][1]
    choice = ChoiceUseItem(item)
    if choice == True:
            giveItemEffects(user_details,item)
    else:
        print(item,'securely stored in backpack.')
    
    return
        

def ChoiceUseItem(item):
    
    print('Do you want to use',item['Name'],'?')
    while True:
        choice = input('Enter [Y/N]: ')
        choice = choice.upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print('Enter \'Y\' or \'N\' only')
            continue
    
    return


def giveItemEffects(user_details,item):
    
    if item['Name'] == 'HP Potion':
        HP_Potion(user_details, item)
    elif item['Name'] == 'Attack Boost':
        Attack_Boost(user_details, item)
    
    return
        

def HP_Potion(user_details,item):
    
    import random
    
    user_pokemon = user_details['Starter Pokemon']
    
    print('Your',user_pokemon['Name'],'\'s Health:',user_pokemon['HP'])
    
    if user_pokemon['HP'] < user_pokemon['Max HP']:
        
        #Adding 30% of MAX HP
        health_add = (30 / 100) * user_pokemon['Max HP']
        health_add += random.radnint(10,15)
        health_add=round(health_add)
        user_pokemon['HP'] += health_add
        
        if user_pokemon['HP'] > user_pokemon['Max HP']:
            user_pokemon['HP'] = user_pokemon['Max HP']
        
        #Status of Item: Used
        user_details['Items'][1]['Status'] = 'Used'
    
    elif user_pokemon['HP'] == user_pokemon['Max HP']:
        
        print('Cannot Heal! Pokemon already at Full HP.')
        PythonGrammar.TimePause()
    
    PythonGrammar.Loading('Drinking Health Potion')
    
    print('Your',user_pokemon['Name'],'\'s Health after consuming HP Potion:',user_pokemon['HP'])
    
    return


def Attack_Boost(user_details,item):
    
    user_pokemon = user_details['Starter Pokemon']
    user_attacks_dic = user_pokemon['Attacks']
    
    print('Your',user_pokemon['Name'],'Attack Stats are:')
    
    for i in user_attacks_dic:
        PythonGrammar.displayBlankLine()
        print(i,'.',sep='',end='') #Serial No.
        print('Name:',i['Name'])
        print('Damage:',i['Damage'])
    
    #Boosting Attack Stats by 30%
    for i in user_attacks_dic:
        i['Damage'] += (30/100) * i['Damage']
    
    user_details['Items'][1]['Status'] = 'Used'
    
    PythonGrammar.Loading('Using Attack Boost')
    
    print('Your',user_pokemon['Name'],'Attack Stats after consuming Attack Boost are:')
    
    for i in user_attacks_dic:
        PythonGrammar.displayBlankLine()
        print(i,'.',sep='',end='') #Serial No.
        print('Name:',i['Name'])
        print('Damage:',i['Damage'])
    
    return
import PythonGrammar

def giveAttackStats(user_details):
    
    '''This function Updates the Pokemon and gives it 'Attack' Category.'''
    
    user_pokemon = user_details['Starter Pokemon']
    
    #User Pokemon Attack Stats
    user_scratch_damage, user_scratch_count, user_scratch_type = 5,20,'Normal'
    user_ember_damage, user_ember_count, user_ember_type = 7,7,'Fire'
    user_watergun_damage, user_watergun_count, user_watergun_type = 7,5,'Water'
    user_bulletseed_damage, user_bulletseed_count, user_bulletseed_type = 7,3,'Grass'
    user_tackle_damage, user_tackle_count, user_tackle_type = 6,15,'Normal'
    
    #User Attack Dictionary
    user_attacks_dic={}
    
    #Scratch
    user_attacks_dic[1]={}
    user_attacks_dic[1]['Name'] = 'Scratch'
    user_attacks_dic[1]['Damage'] = user_scratch_damage
    user_attacks_dic[1]['Type'] = user_scratch_type
    user_attacks_dic[1]['Count'] = user_scratch_count
    
    #Ember/Water Gun/Bullet Seed
    user_attacks_dic[2]={}
    
    #EMBER
    if user_pokemon['Type'] == 'Fire':
        user_attacks_dic[2]['Name'] = 'Ember'
        user_attacks_dic[2]['Damage'] = user_ember_damage
        user_attacks_dic[2]['Type'] = user_ember_type
        user_attacks_dic[2]['Count'] = user_ember_count
    
    #WATER GUN
    elif user_pokemon['Type'] == 'Water':
        user_attacks_dic[2]['Name'] = 'Water Gun'
        user_attacks_dic[2]['Damage'] = user_watergun_damage
        user_attacks_dic[2]['Type'] = user_watergun_type
        user_attacks_dic[2]['Count'] = user_watergun_count
    
    #BULLET SEED
    elif user_pokemon['Type'] == 'Grass':
        user_attacks_dic[2]['Name'] = 'Bullet Seed'
        user_attacks_dic[2]['Damage'] = user_bulletseed_damage
        user_attacks_dic[2]['Type'] = user_bulletseed_type
        user_attacks_dic[2]['Count'] = user_bulletseed_count
    
    #Tackle
    user_attacks_dic[3]={}
    user_attacks_dic[3]['Name'] = 'Tackle'
    user_attacks_dic[3]['Damage'] = user_tackle_damage
    user_attacks_dic[3]['Type'] = user_tackle_type
    user_attacks_dic[3]['Count'] = user_tackle_count
    
    #user_attacks_counter is used to keep track of total no. of time an attack can be used. (total counter of attack)
    user_attacks_counter={}
    
    user_attacks_counter['Scratch'] = user_attacks_dic[1]['Count']
    
    pokemon_type = user_pokemon['Type']
    if pokemon_type == 'Fire':
        user_attacks_counter['Ember'] = user_attacks_dic[2]['Count']
    
    elif pokemon_type == 'Water':
        user_attacks_counter['Water Gun'] = user_attacks_dic[2]['Count']
    
    elif pokemon_type == 'Grass':
        user_attacks_counter['Bullet Seed'] = user_attacks_dic[2]['Count']
    
    user_attacks_counter['Tackle'] = user_attacks_dic[3]['Count']
    
    #Adding Attack Dictionary to Pokemon
    user_pokemon['Attacks'] = user_attacks_dic
    user_pokemon['Attacks Counter'] = user_attacks_counter
    
    return


def displayAttackChoice(user_details):
    
    user_pokemon = user_details['Starter Pokemon']
    user_attacks_dic = user_pokemon['Attacks']
    user_attacks_counter = user_pokemon['Attacks Counter']
    
    print('Choose Your Attack:')
    PythonGrammar.displayBlankLine()
    
    print('1. Scratch','\t\t',user_attacks_dic[1]['Count'],'/',user_attacks_counter['Scratch']) #This displays: 1. Scratch 19/20
    special_name = user_attacks_dic[2]['Name']
    print('2.',special_name,'\t\t',user_attacks_dic[2]['Count'],'/',user_attacks_counter[special_name])
    print('3. Tackle','\t\t',user_attacks_dic[3]['Count'],'/',user_attacks_counter['Tackle'])
    
    '''if user_pokemon['Type']=='Fire':
        print('2. Ember','\t\t',user_attacks_dic[2]['Count'],'/',user_attacks_counter['Ember'])
    elif user_pokemon['Type']=='Water':
        print('2. Water Gun','\t\t',user_attacks_dic[2]['Count'],'/',user_attacks_counter['Water Gun'])
    elif user_pokemon['Type']=='Grass':
        print('2. Bullet Seed','\t\t',user_attacks_dic[2]['Count'],'/',user_attacks_counter['Bullet Seed'])
    '''
    
    return


def checkAttackExhausted(user_attack):
    
    if user_attack['Count'] <= 0:
        return True


def displayAttackExhausted():
    
    PythonGrammar.displayBlankLine()
    print('This attack is exhausted. Select another attack option.')
    PythonGrammar.displayBlankLine()
    
    return


def Choice(user_details):
    
    user_pokemon = user_details['Starter Pokemon']
    user_attacks_dic = user_pokemon['Attacks']
    
    #Getting Choice
    c = None
    while True:
        
        displayAttackChoice(user_details)
        c = input('Enter your choice (1-3): ')
        
        if c in ['1','2','3']:
            c = int(c)
            user_attack = user_attacks_dic[c]
            
            if checkAttackExhausted(user_attack):
                displayAttackExhausted(user_attack)
                continue
            else:
                break
        else:
            print('Enter a choice in the range (1-3) only.')
            continue
    
    return user_attacks_dic[c]
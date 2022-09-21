import PythonGrammar

def display(wild_pokemon):
    
    PythonGrammar.displayBlankLine()
    print('Wild Pokemon Name:',wild_pokemon['Name'])
    print('Wild Pokemon Type:',wild_pokemon['Type'])
    print('Wild Pokemon HP:',wild_pokemon['HP'])
    PythonGrammar.displayBlankLine()
    PythonGrammar.TimePause()
    
    return


def WildPokemon():
    
    wild_dic={}
    
    #Wild Pidgey
    wild_dic[1]={}
    wild_dic[1]['Name'] = 'Pidgey'
    wild_dic[1]['Type'] = 'Flying'
    wild_dic[1]['HP'] = 80
    wild_dic[1]['Max HP'] = 80
    wild_dic[1]['XP'] = 0
    wild_dic[1]['Max XP'] = 100
    wild_dic[1]['Current Form'] = 1
    wild_dic[1]['2nd Form'] = 'Pigeotto'
    wild_dic[1]['3rd Form'] = 'Pidgeot'
    
    #Wild Pichu
    wild_dic[2]={}
    wild_dic[2]['Name'] = 'Pichu'
    wild_dic[2]['Type'] = 'Electric'
    wild_dic[2]['HP'] = 80
    wild_dic[2]['Max HP'] = 80
    wild_dic[2]['XP'] = 0
    wild_dic[2]['Max XP'] = 100
    wild_dic[2]['Current Form'] = 1
    wild_dic[2]['2nd Form'] = 'Pikachu'
    wild_dic[2]['3rd Form'] = 'Raichu'
    
    #Wild Caterpie
    wild_dic[3]={}
    wild_dic[3]['Name'] = 'Caterpie'
    wild_dic[3]['Type'] = 'Bug'
    wild_dic[3]['HP'] = 60
    wild_dic[3]['Max HP'] = 60
    wild_dic[3]['XP'] = 0
    wild_dic[3]['Max XP'] = 100
    wild_dic[3]['Current Form'] = 1
    wild_dic[3]['2nd Form'] = 'Metapod'
    wild_dic[3]['3rd Form'] = 'Butterfree'
    
    #Wild Rattata
    wild_dic[4]={}
    wild_dic[4]['Name'] = 'Rattata'
    wild_dic[4]['Type'] = 'Normal'
    wild_dic[4]['HP'] = 60
    wild_dic[4]['Max HP'] = 60
    wild_dic[4]['XP'] = 0
    wild_dic[4]['Max XP'] = 100
    wild_dic[4]['Current Form'] = 1
    wild_dic[4]['2nd Form'] = 'Raticate'
    wild_dic[4]['3rd Form'] = None

    return wild_dic


def get():
    
    import random
    
    #Getting Random Wild Pokemon
    wild_dic = WildPokemon()
    n = random.randint(1,len(wild_dic))
    wild_pokemon = wild_dic[n]
    
    return wild_pokemon


def giveAttackStats(wild_pokemon):
    
    '''This function Updates Wild Pokemon and gives it 'Attack' Category.'''
    
    #Wild Pokemon Attack Stats
    wild_scratch_damage, wild_scratch_count, wild_scratch_type = 5,20,'Normal' #SCRATCH
    wild_gust_damage, wild_gust_count, wild_gust_type  = 7,7,'Flying'        #GUST
    wild_thundershock_damage, wild_thundershock_count, wild_thundershock_type  = 7,6,'Electric' #THUNDER SHOCK
    wild_tackle_damage, wild_tackle_count , wild_tackle_type = 6,15,'Normal'   #TACKLE
    wild_quickattack_damage, wild_quickattack_count , wild_quickattack_type = 9,15,'Normal'   #QUICK ATTACK
    
    #WILD POKEMON Attack Dictionary
    wild_attacks_dic={}
    
    #Scratch
    wild_attacks_dic[1]={}
    wild_attacks_dic[1]['Name'] = 'Scratch'
    wild_attacks_dic[1]['Damage'] = wild_scratch_damage
    wild_attacks_dic[1]['Type'] = wild_scratch_type
    wild_attacks_dic[1]['Count'] = wild_scratch_count
    
    #Gust/Thunder Shock/Quick Attack
    wild_attacks_dic[2]={}
    
    #GUST
    if wild_pokemon['Type'] == 'Flying':
        wild_attacks_dic[2]['Name'] = 'Gust'
        wild_attacks_dic[2]['Damage'] = wild_gust_damage
        wild_attacks_dic[2]['Type'] = wild_gust_type
        wild_attacks_dic[2]['Count'] = wild_gust_count
    
    #THUNDER SHOCK
    elif wild_pokemon['Type'] == 'Electric':
        wild_attacks_dic[2]['Name'] = 'Thunder Shock'
        wild_attacks_dic[2]['Damage'] = wild_thundershock_damage
        wild_attacks_dic[2]['Type'] = wild_thundershock_type
        wild_attacks_dic[2]['Count'] = wild_thundershock_count
    
    #QUICK ATTACK
    elif wild_pokemon['Type'] == 'Normal':
        wild_attacks_dic[2]['Name'] = 'Quick Attack'
        wild_attacks_dic[2]['Damage'] = wild_quickattack_damage
        wild_attacks_dic[2]['Type'] = wild_quickattack_type
        wild_attacks_dic[2]['Count'] = wild_quickattack_count
    
    #Tackle
    wild_attacks_dic[3]={}
    wild_attacks_dic[3]['Name'] = 'Tackle'
    wild_attacks_dic[3]['Damage'] = wild_tackle_damage
    wild_attacks_dic[3]['Type'] = wild_tackle_type
    wild_attacks_dic[3]['Count'] = wild_tackle_count
    
    #user_attacks_counter is used to keep track of total no. of times an attack can be used.
    wild_attacks_counter={}
    
    wild_attacks_counter['Scratch'] = wild_attacks_dic[1]['Count']
    
    wild_type = wild_pokemon['Type']
    if wild_type == 'Flying':
        wild_attacks_counter['Gust'] = wild_attacks_dic[2]['Count']
    
    elif wild_type == 'Electric':
        wild_attacks_counter['Thunder Shock'] = wild_attacks_dic[2]['Count']
    
    elif wild_type == 'Normal':
        wild_attacks_counter['Quick Attack'] = wild_attacks_dic[2]['Count']
    
    wild_attacks_counter['Tackle'] = wild_attacks_dic[3]['Count']
    
    #Adding Attack Dictionary to Wild Pokemon
    wild_pokemon['Attacks'] = wild_attacks_dic
    wild_pokemon['Attacks Counter'] = wild_attacks_counter
    
    return

def AttackChoice(wild_pokemon):
    
    import random
    
    wild_attacks_dic = wild_pokemon['Attacks']
    
    n = 0
    while True:
        n = random.randint(1,len(wild_attacks_dic))
        wild_attack = wild_attacks_dic[n]   #This is a dictionary containing NAME, DAMAGE, COUNT values of attack.
        if wild_attack['Count'] <= 0:        #If attack is exhausted
            continue
        else:
            break
    
    return wild_attacks_dic[n]
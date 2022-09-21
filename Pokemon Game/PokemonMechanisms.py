import PythonGrammar
import random


def XPRandomiser(max_xp):
    
    a = max_xp/20
    x = random.randint(-a,+a)
    x += random.randint(-a+3,a+5) - (a+1,a+2)
    return x


def displayXP(user_pokemon,xp_add):
    
    PythonGrammar.displayBlankLine()
    print(user_pokemon['Name'],'has gained',xp_add,'XP.')
    print('Current XP:',user_pokemon['XP'],'/',user_pokemon['Max HP'])
    PythonGrammar.TimePause()
    
    return


def giveXP(user_details,win):
    
    '''Giving XP to Pokemon after Battle'''
    
    user_pokemon = user_details['Starter Pokemon']
    max_xp = user_pokemon['Max XP']
    xp_add = 0
    
    if win == True:
        
        #50% of Max XP given if win
        xp_add = (50/100) * max_xp
        xp_add += XPRandomiser()
        
    else:
        
        #25% of Max HP given if lose
        xp_add = (25/100) * max_xp
        xp_add += XPRandomiser()
        
    xp_add = round(xp_add)
    user_pokemon['XP'] += xp_add
    
    displayXP(user_pokemon,xp_add)
    
    #If XP > Max XP
    if user_pokemon['XP'] > user_pokemon['Max XP']:
        LevelUp(user_details)
    else:
        more_xp = user_pokemon['Max XP']-user_pokemon['XP']
        level = user_pokemon['Level']
        print(more_xp,'more XP to reach Level',(level+1))
    
    PythonGrammar.displayBlankLine()
    PythonGrammar.displayLine()
    
    return


def displayLevelUp(user_pokemon):
    
    print('Your',user_pokemon['Name'],' is levelling up. You have no choice but to witness the growth.')
    PythonGrammar.Loading(user_pokemon['Name'] + 'is Levelling Up')
    print('Your',user_pokemon['Name'],'is now Level',user_pokemon['Level'])
    print('Current XP:',user_pokemon['XP'],'/',user_pokemon['Max XP'])
    PythonGrammar.TimePause()
    
    return
    
    
def LevelUp(user_details):
    
    user_pokemon = user_details['Starter Pokemon']
    
    #Performing Leveling Up Calculations
    user_pokemon['Level'] += 1
    extra_xp = user_pokemon['Max XP'] - user_pokemon['XP']
    user_pokemon['XP'] = extra_xp
    user_pokemon['Max XP'] += (20/100) * user_pokemon['Max XP'] #New Max XP = 1.2x previous Max XP
    
    displayLevelUp(user_pokemon)
    
    increaseAttack(user_pokemon)
    increaseHP(user_pokemon)
    
    FullHeal(user_pokemon)
    RefreshAttackCounters(user_pokemon)
    
    #Evolving Pokemon if it crosses a certain level
    if user_pokemon['Level'] in [user_pokemon['2nd Form Level',user_pokemon['3rd Form Level']]]:
        Evolve(user_details)
    
    return


def Damage_Add(dmg):
    
    damage_add = (40/100) * dmg
    damage_add += random.randint(-(10/100)*dmg,(20/100)*dmg)
    damage_add += random.randint((30/100)*dmg,(50/100)*dmg)
    damage_add -+ random.randint((10/100)*dmg,(30/100)*dmg)
    damage_add = round(damage_add)
    
    return damage_add
    
    
def increaseAttack(user_pokemon):
    
    #Increasing Attack Stats
    user_attacks_dic = user_pokemon['Attacks']
    
    PythonGrammar.Loading('Increasing Attack Stats')
    
    old_damage = new_damage = None
    
    for i in user_attacks_dic:
        
        old_damage = user_attacks_dic[i]['Damage']
        
        user_attacks_dic[i]['Damage'] += Damage_Add(old_damage)
        
        new_damage = user_attacks_dic[i]['Damage']
        
        displayIncreaseDamage(old_damage,new_damage,user_attacks_dic[i]['Name'])
    
    else:
        
        print('Attack Damage Increased Successfully.')
        PythonGrammar.displayBlankLine()
    
    return


def displayIncreaseDamage(old_damage,new_damage,attack_name):
    
    print(attack_name,'had a Damage of:',old_damage)
    print('Damage Increase: +',(new_damage-old_damage))
    print('Current Damage of',attack_name,':',new_damage)
    PythonGrammar.TimePause()
    PythonGrammar.displayBlankLine()
    
    return


def HP_Add(old_max_hp):
    
    hp_add = (20/100) * old_max_hp
    hp_add += random.randint(-(5/100) * old_max_hp,+(5/100) * old_max_hp)
    hp_add += random.randint((10/100) * old_max_hp,+(25/100) * old_max_hp)
    hp_add -= random.randint((5/100) * old_max_hp,+(10/100) * old_max_hp)
    hp_add = round(hp_add)
    
    return hp_add


def increaseHP(user_pokemon):
    
    #Increasing Max HP
    old_max_hp = user_pokemon['Max HP']
    
    user_pokemon['Max HP'] += HP_Add(old_max_hp)
    
    new_max_hp = user_pokemon['Max HP']
    
    displayIncreaseHP(old_max_hp,new_max_hp)
    
    return


def displayIncreaseHP(old_max_hp,new_max_hp):
    
    print('Previous HP:',old_max_hp)
    print('New HP:',new_max_hp)
    PythonGrammar.TimePause()
    PythonGrammar.displayBlankLine()
    
    return

    
def FullHeal(user_pokemon):
    
    #Fully Healing Pokemon
    PythonGrammar.Loading('Fully Healing Pokemon')
    user_pokemon['HP'] = user_pokemon['Max HP']  
    
    return


def displayRefresh(attack_name):
    
    PythonGrammar.displayBlankLine()
    print(attack_name,'Successfully Refreshed.')
    PythonGrammar.displayBlankLine()
    PythonGrammar.TimePause()
    
    return


def RefreshAttackCounters(user_pokemon):
        
    #Refreshing Attack Counters
    PythonGrammar.Loading('Refreshing Attack Counters')
        
    user_attacks_dic = user_pokemon['Attacks']
    user_attacks_counter = user_pokemon['Attacks Counter']
        
    for i in user_attacks_dic:
        
        attack_name = user_attacks_dic[i]['Name']
        attack_counter = user_attacks_counter[attack_name]
        user_attacks_dic[i]['Count'] = attack_counter
        
        displayRefresh(attack_name)
        
    else:
        
        print('Attacks successfully Refreshed.')
        PythonGrammar.TimePause()
        PythonGrammar.displayBlankLine()
        PythonGrammar.TimePause()
        
    return


def Evolve(user_details):
    
    user_pokemon = user_details['Starter Pokemon']
    pokemon_name = user_pokemon['Name']
    
    print('Your',pokemon_name,'is evolving. There is nothing you can do but witness the evolution.')
    
    #Evolving Pokemon
    next_form = user_pokemon['Current Form'] + 1
    form2 = user_pokemon['2nd Form']
    form3 = user_pokemon['3rd Form']
    
    if next_form == 2:
        
        if form2 != None:
            
            print(pokemon_name,'is evolving into:',form2)
            user_pokemon['Name'] = form2
            increaseAttack(user_pokemon)
            increaseHP(user_pokemon)
            user_pokemon['Current Form'] += 1
            
        else:
            print(user_pokemon['Name'],'has already reached the last evolution.')
        
    elif next_form == 3:
        
        if form3 != None:
            
            print(pokemon_name,'is evolving into:',user_pokemon['3rd Form'])
            user_pokemon['Name'] = form3
            increaseAttack(user_pokemon)
            increaseHP(user_pokemon)
            user_pokemon['Current Form'] += 1
            
        else:
            print(user_pokemon['Name'],'has already reached the last evolution.')
    
    elif next_form == 4: #MEGA Evolution. Block to be updated
        pass
    
    else:
        print(user_pokemon['Name'],'has already reached the last evolution.')
    
    PythonGrammar.TimePause()
    
    return
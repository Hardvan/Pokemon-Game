import PythonGrammar
import random
    
def Multiplier(attack_type,pokemon_type):
    
    multiplier = 1
    
    #NORMAL
    if attack_type == 'Normal':
        #Not Very Effective
        if pokemon_type in ['Rock','Steel']: multiplier = 0.5
        #0 Effective
        elif pokemon_type in ['Ghost']: multiplier = 0
    
    #FIRE
    elif attack_type == 'Fire':
        #Not Very Effective
        if pokemon_type in ['Fire','Water','Rock','Dragon']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Grass','Ice','Bug','Steel']: multiplier = 2
        
    #WATER
    elif attack_type == 'Water':
        #Not Very Effective
        if pokemon_type in ['Water','Grass','Dragon']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Fire','Ground','Rock']: multiplier = 2
        
    #ELECTRIC
    elif attack_type == 'Electric':
        #Not Very Effective
        if pokemon_type in ['Electric','Grass','Dragon']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Water','Flying']: multiplier = 2
        #0 Effective
        elif pokemon_type in ['Ground']: multiplier = 0
        
    #GRASS
    elif attack_type == 'Grass':
        #Not Very Effective
        if pokemon_type in ['Fire','Grass','Poison','Flying','Bug','Dragon','Steel']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Water','Ground','Rock']: multiplier = 2
    
    #ICE
    elif attack_type == 'Ice':
        #Not Very Effective
        if pokemon_type in ['Fire','Water','Ice','Steel']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Grass','Ground','Flying','Dragon']: multiplier = 2
    
    #FIGHTING
    elif attack_type == 'Fighting':
        #Not Very Effective
        if pokemon_type in ['Poison','Flying','Psychic','Bug','Fairy']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Normal','Ice','Rock','Dark','Steel']: multiplier = 2
        #0 Effective
        if pokemon_type in ['Ghost']: multiplier = 0
    
    #POISON
    elif attack_type == 'Poison':
        #Not Very Effective
        if pokemon_type in ['Poison','Ground','Rock','Ghost']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Fairy']: multiplier = 2
        #0 Effective
        if pokemon_type in ['Steel']: multiplier = 0
    
    #GROUND
    elif attack_type == 'Ground':
        #Not Very Effective
        if pokemon_type in ['Grass','Bug']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Fire','Electric','Poison','Rock','Steel']: multiplier = 2
        #0 Effective
        if pokemon_type in ['Flying']: multiplier = 0
    
    #FLYING
    elif attack_type == 'Flying':
        #Not Very Effective
        if pokemon_type in ['Electric','Rock','Steel']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Grass','Fighting','Bug']: multiplier = 2
    
    #PSYCHIC
    elif attack_type == 'Psychic':
        #Not Very Effective
        if pokemon_type in ['Psychic','Steel']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Fighting','Poison']: multiplier = 2
        #0 Effective
        if pokemon_type in ['Dark']: multiplier = 0
    
    #BUG
    elif attack_type == 'Bug':
        #Not Very Effective
        if pokemon_type in ['Fire','Fighting','Poison','Flying','Ghost','Steel','Fairy']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Grass','Psychic','Dark']: multiplier = 2
    
    #ROCK
    elif attack_type == 'Rock':
        #Not Very Effective
        if pokemon_type in ['Fighting','Ground','Steel']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Fire','Ice','Flying','Bug']: multiplier = 2
    
    #GHOST
    elif attack_type == 'Ghost':
        #Not Very Effective
        if pokemon_type in ['Dark']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Psychic','Ghost']: multiplier = 2
        #0 Effective
        if pokemon_type in ['Normal']: multiplier = 0
    
    #DRAGON
    elif attack_type == 'Dragon':
        #Not Very Effective
        if pokemon_type in ['Steel']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Dragon']: multiplier = 2
        #0 Effective
        if pokemon_type in ['Fairy']: multiplier = 0
    
    #DARK
    elif attack_type == 'Dark':
        #Not Very Effective
        if pokemon_type in ['Fighting','Dark','Fairy']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Psychic','Ghost']: multiplier = 2
    
    #STEEL
    elif attack_type == 'Steel':
        #Not Very Effective
        if pokemon_type in ['Fire','Water','Electric','Steel']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Ice','Rock','Fairy']: multiplier = 2
    
    #FAIRY
    elif attack_type == 'Fairy':
        #Not Very Effective
        if pokemon_type in ['Fire','Poison','Steel']: multiplier = 0.5
        #Super Effective
        elif pokemon_type in ['Fighting','Dragon','Dark']: multiplier = 2
    
    displayEffective(multiplier)
    
    return multiplier


def displayEffective(multiplier):
    
    if multiplier > 1: #Super Effective
        PythonGrammar.displayBlankLine()
        print('It was super effective!')
    elif multiplier < 1: #Not Very Effective
        PythonGrammar.displayBlankLine()
        print('It was not very effective.')
        PythonGrammar.displayBlankLine()
    
    return


def DamageRandomiser():
    
    #Randomising Damage. x is in range [-2,8]
    x = random.randint(1,6) - random.randint(2,5) + random.randint(2,4)
    return x


def MultiplierRandomiser():
    
    #Randomising Multiplier
    x = round(random.uniform(0.80,1.20),2) # MAX: x1.20, MIN: x0.80
    return x
    
    
def Damage(attack_dic,multiplier):
    
    
    #Calculating Damage
    dmg = attack_dic['Damage']
    
    x = DamageRandomiser()
    dmg += x 
    
    multiplier *= MultiplierRandomiser()
    dmg *= multiplier
    
    #Critical Hit
    crit = CriticalHit(dmg)
    
    
    dmg += crit
    dmg = round(dmg)
    
    return dmg


def CriticalHit(dmg):
    
    crit = 0
    chance = getCritChance()
    if chance == True:
        print('It was a critical hit!')
        PythonGrammar.displayBlankLine()
        crit = dmg + CritRandomiser()
    else:
        crit = 0
    
    return crit

def CritRandomiser():
    
    x = random.randint(10,20) + random.randint(3,5) + random.randint(1,4) - random.randint(3,5) - random.randint(4,6)
    return x
    
def getCritChance():
    
    n = random.randint(1,6)
    if n in [5,6]: #33% Probabilty of Critical Hit
        return True
    
    












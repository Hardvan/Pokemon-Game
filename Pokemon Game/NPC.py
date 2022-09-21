import PythonGrammar

def display(npc_details):
    
    npc_name = npc_details['Name']
    npc_pokemon = npc_details['Pokemon']
    
    PythonGrammar.displayLine()
    PythonGrammar.displayBlankLine()
    print('NPC Name:',npc_name)
    print('NPC Pokemon:',npc_pokemon['Name'])
    print('NPC Pokemon Type:',npc_pokemon['Type'])
    print('NPC Pokemon HP:',npc_pokemon['HP'])
    PythonGrammar.displayBlankLine()
    PythonGrammar.TimePause()
    
    return

def NPC():
    
    npc_dic={}  #Dictionary to store details of all NPCs
                #Name, Pokemon
    
    #Nested Dictionary
    npc_dic[1]={}
    npc_dic[2]={}
    npc_dic[3]={}
    
    #Storing Name
    npc_dic[1]['Name'] = 'Mark'
    npc_dic[2]['Name'] = 'Peter'
    npc_dic[3]['Name'] = 'Ash'
    
    #Storing Pokemon Details
    
    #Mark's Pokemon
    npc_dic[1]['Pokemon']={}
    npc_dic[1]['Pokemon']['Name'] = 'Charmander'
    npc_dic[1]['Pokemon']['Type'] = 'Fire'
    npc_dic[1]['Pokemon']['HP'] = 80
    npc_dic[1]['Pokemon']['Max HP'] = 80
    
    #Peter's Pokemon
    npc_dic[2]['Pokemon']={}
    npc_dic[2]['Pokemon']['Name'] = 'Squirtle'
    npc_dic[2]['Pokemon']['Type'] = 'Water'
    npc_dic[2]['Pokemon']['HP'] = 80
    npc_dic[2]['Pokemon']['Max HP'] = 80
    
    #Ash's Pokemon
    npc_dic[3]['Pokemon']={}
    npc_dic[3]['Pokemon']['Name'] = 'Bulbasaur'
    npc_dic[3]['Pokemon']['Type'] = 'Grass'
    npc_dic[3]['Pokemon']['HP'] = 80
    npc_dic[3]['Pokemon']['Max HP'] = 80
    
    return npc_dic #Returns all NPCs

def getNPC():
    
    import random
    
    npc_dic = NPC()
    n = random.randint(1,3)
    npc_details = npc_dic[n]
    
    #Returning Dictionary of the chosen NPC
    return npc_details

def NPCPokemonAttackStats(npc_details):
    
    '''This function Updates NPC Pokemon and gives it 'Attack' Category.'''
    
    npc_pokemon = npc_details['Pokemon']
    
    #NPC Pokemon Attack Stats
    npc_scratch_damage, npc_scratch_count, npc_scratch_type = 5, 20, 'Normal'
    npc_ember_damage, npc_ember_count, npc_ember_type = 7, 7, 'Fire'
    npc_watergun_damage, npc_watergun_count, npc_watergun_type = 7, 5, 'Water'
    npc_bulletseed_damage, npc_bulletseed_count, npc_bulletseed_type = 7, 3, 'Grass'
    npc_tackle_damage, npc_tackle_count, npc_tackle_type = 6, 15, 'Normal'
    
    #NPC Attack Dictionary
    npc_attacks_dic={}
    
    #Scratch
    npc_attacks_dic[1]={}
    npc_attacks_dic[1]['Name'] = 'Scratch'
    npc_attacks_dic[1]['Damage'] = npc_scratch_damage
    npc_attacks_dic[1]['Type'] = npc_scratch_type
    npc_attacks_dic[1]['Count'] = npc_scratch_count
    
    #Ember/Water Gun/Bullet Seed
    npc_attacks_dic[2]={}
    
    #EMBER
    if npc_pokemon['Type'] == 'Fire':
        npc_attacks_dic[2]['Name'] = 'Ember'
        npc_attacks_dic[2]['Damage'] = npc_ember_damage
        npc_attacks_dic[2]['Type'] = npc_ember_type
        npc_attacks_dic[2]['Count'] = npc_ember_count
    
    #WATER GUN
    elif npc_pokemon['Type'] == 'Water':
        npc_attacks_dic[2]['Name'] = 'Water Gun'
        npc_attacks_dic[2]['Damage'] = npc_watergun_damage
        npc_attacks_dic[2]['Type'] = npc_watergun_type
        npc_attacks_dic[2]['Count'] = npc_watergun_count
    
    #BULLET SEED
    elif npc_pokemon['Type']=='Grass':
        npc_attacks_dic[2]['Name'] = 'Bullet Seed'
        npc_attacks_dic[2]['Damage'] = npc_bulletseed_damage
        npc_attacks_dic[2]['Type'] = npc_bulletseed_type
        npc_attacks_dic[2]['Count'] = npc_bulletseed_count
    
    #Tackle
    npc_attacks_dic[3]={}
    npc_attacks_dic[3]['Name'] = 'Tackle'
    npc_attacks_dic[3]['Damage'] = npc_tackle_damage
    npc_attacks_dic[3]['Type'] = npc_tackle_type
    npc_attacks_dic[3]['Count'] = npc_tackle_count
    
    #Adding Attack Dictionary to NPC Pokemon
    npc_details['Pokemon']['Attacks'] = npc_attacks_dic
    
    return

def AttackChoice(npc_details):
    
    import random
    
    npc_attacks_dic = npc_details['Pokemon']['Attacks']
    
    n = 0
    while True:
        n = random.randint(1,3)
        npc_attack = npc_attacks_dic[n]   #This is a dictionary containing NAME and DAMAGE values of attack.
        if npc_attack['Count'] <= 0:      #If attack is exhausted
            continue
        else:
            break
    
    return npc_attacks_dic[n]
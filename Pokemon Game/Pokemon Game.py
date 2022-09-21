import PythonGrammar
import ReadyConfirmExits
import NicknameStarterPokemon
import UserPokemonAttack
import NPC
import BattleMechanics
import GuessTheNumberGame
import WildPokemon,WildPokemonCapture
import Villager
import RockPaperScissorsVillager
import PokemonMechanisms
import PokemonCenter
import Item


def getUserDictionary():
    
    #Dictionary to store all user Details
    user_details = {}
    user_details['Name'] = NicknameStarterPokemon.Nickname()
    user_details['Starter Pokemon'] = NicknameStarterPokemon.StarterPokemon()
    user_details['Pokeballs'] = 10
    
    return user_details
    

def MainFunction():
    
    #MAIN GAME FUNCTIONS
    
    #Briefing with Story
    Introduction()
    
    #User Details Dictionary
    user_details = getUserDictionary()
    
    #Getting Attack Parameters of User Pokemon
    UserPokemonAttack.giveAttackStats(user_details)
    
    #Battle With NPC
    NPCBattle(user_details)
    
    #Healing Pokemon After Battle
    PostBattle(user_details)
    
    #Battle with WILD POKEMON
    WildPokemonBattle(user_details)
    
    #Random Encounter with Villager
    EncounterVillager(user_details)
    
    #Battle with GYM LEADER
    #GymLeader(user_details)
    

def Introduction():
    
    #Briefing the story
    print('WELCOME TO HARDIK\'S POKEMON GAME!')
    PythonGrammar.TimePause()
    ReadyConfirmExits.Ready()
    
    PythonGrammar.displayLine()
    PythonGrammar.displayBlankLine()
    print('FRIENDLY AI: Wakey wakey!')
    print('FRIENDLY AI: You have awoken from a deep slumber.')
    print('FRIENDLY AI: The world has been infested with mad monsters made by a mad scientist.')
    print('FRIENDLY AI: Hurry sleephyhead, we don\'t have much time!')

    return


def NPCBattle(user_details):
    
    #Battle with NPC
    win = False
    
    #User Details
    user_name = user_details['Name']
    user_pokemon = user_details['Starter Pokemon']
    
    #Getting NPC Details
    npc_details = NPC.getNPC() #NPC Name and NPC Pokemon
    npc_name = npc_details['Name']
    npc_pokemon = npc_details['Pokemon']
    
    #Displaying NPC Details
    NPC.display(npc_details)
    
    #NPC Pokemon Attack Stats
    NPC.NPCPokemonAttackStats(npc_details)
        
    #BATTLE STARTS!
    
    #Loop For Battle, which terminates when Pokemon HP <= 0
    while True:
        
        #This is a dictionary containing NAME and DAMAGE values of attack.
        user_attack = UserPokemonAttack.Choice(user_details)
    
        #NPC Choosing Attack
        npc_attack = NPC.AttackChoice(npc_details)
        
        #Attack Multipliers based on Attack Chosen
        user_attack_multiplier = BattleMechanics.Multiplier(user_attack['Type'],npc_pokemon['Type'])
        npc_attack_multiplier = BattleMechanics.Multiplier(npc_attack['Type'],user_pokemon['Type'])
        
        #Calculating...
        PythonGrammar.Loading('Calculating')
        
        #USER ATTACKING
        
        print(npc_name,'\'s',npc_pokemon['Name'],'health:',npc_pokemon['HP'])
        PythonGrammar.displayBlankLine()
        print('You have used:',user_attack['Name'])
        PythonGrammar.TimePause()
        
        #Calculating Damage
        dmg = BattleMechanics.Damage(user_attack,user_attack_multiplier)
        npc_pokemon['HP'] -= dmg
        user_attack['Count'] -= 1 #Reducing the attack counter. Example 20/20 becomes 19/20
        
        if npc_pokemon['HP'] < 0: #HP can't be -10
            npc_pokemon['HP'] = 0
        
        print('Damage on enemy',npc_pokemon['Name'],':',dmg)
        PythonGrammar.displayBlankLine()
        print(npc_name,'\'s',npc_pokemon['Name'],'health after',user_attack['Name'],':',npc_pokemon['HP'])
        
        if npc_pokemon['HP'] == 0: #Exiting the Loop if Opponent Pokemon HP<=0
            win = True    
            PythonGrammar.displayBlankLine()    
            print(npc_name,'\'s',npc_pokemon['Name'],'has fainted.')
            print('YOU WON!')
            PythonGrammar.displayBlankLine()
            PythonGrammar.displayLine()
            break
        
        PythonGrammar.TimePause()
        
        #NPC ATTACKING
        
        PythonGrammar.displayBlankLine()
        print(user_name,'\'s',user_pokemon['Name'],'health:',user_pokemon['HP'])
        PythonGrammar.displayBlankLine()
        print(npc_name,'has used:',npc_attack['Name'])
        
        PythonGrammar.TimePause()
        
        #Calculating Damage
        dmg = BattleMechanics.Damage(npc_attack,npc_attack_multiplier)
        user_pokemon['HP'] -= dmg
        npc_attack['Count'] -= 1 #Reducing the attack counter. Example 20/20 becomes 19/20

        if user_pokemon['HP'] < 0: #HP can't be -10
            user_pokemon['HP'] = 0        

        print('Damage on your',user_pokemon['Name'],':',dmg)
        PythonGrammar.displayBlankLine()
        print('Your',user_pokemon['Name'],'health after',npc_attack['Name'],':',user_pokemon['HP'])
        PythonGrammar.displayBlankLine()
        
        if user_pokemon['HP'] == 0: #Exiting the Loop if User Pokemon HP<=0
            win = False
            PythonGrammar.displayBlankLine()
            print('Your',user_pokemon,'has fainted.')
            print('YOU LOST.!')
            PythonGrammar.displayBlankLine()
            PythonGrammar.displayLine()
            break
        
        PythonGrammar.TimePause()
        
        #CONTINUE OR ESCAPE the Battle
        exits = ReadyConfirmExits.Exits()
        if exits == True:
            PythonGrammar.Loading('Escaping')
            PythonGrammar.displayLine()
            PythonGrammar.displayBlankLine()
            break
        else:
            PythonGrammar.Loading('Continuing')
            PythonGrammar.displayLine()
            PythonGrammar.displayBlankLine()
            continue
    
    PokemonMechanisms.giveXP(user_details,win)
    
    return


def PostBattle(user_details):
    
    #Healing the Pokemon if user wins the mini game.
    
    win,score = GuessTheNumberGame.play()
    
    if win == True:
        GuessTheNumberGame.HealPokemon(user_details, score)(user_details,score)
    else:
        if GuessTheNumberGame.PlayAgain(user_details) == True:
            PostBattle(user_details)
    
    return


def WildPokemonBattle(user_details):
    
    #Battle with WILD POKEMON
    win = False
    
    #User Details
    user_name = user_details['Name']
    user_pokemon = user_details['Starter Pokemon']
    
    #Getting Wild Pokemon Details
    wild_pokemon = WildPokemon.get() #Wild Pokemon Name, Type, HP, Attacks
    
    #Displaying Wild Pokemon Details
    WildPokemon.display(wild_pokemon)
    
    #Wild Pokemon Attack Stats
    WildPokemon.giveAttackStats(wild_pokemon)
        
    #BATTLE STARTS!
    
    #Loop For Battle, which terminates when Pokemon HP <= 0
    while True:
        
        #This is a dictionary containing NAME and DAMAGE values of attack.
        user_attack = UserPokemonAttack.Choice(user_details)
    
        #Wild Pokemon Choosing Attack
        wild_attack = WildPokemon.AttackChoice(wild_pokemon)
        
        #Attack Multipliers based on Attack Chosen
        user_attack_multiplier = BattleMechanics.Multiplier(user_attack['Type'],wild_pokemon['Type'])
        wild_attack_multiplier = BattleMechanics.Multiplier(wild_attack['Type'],user_pokemon['Type'])
    
        #Calculating...
        PythonGrammar.Loading('Calculating')
        
        #USER ATTACKING
        
        print('Wild',wild_pokemon['Name'],'\'s','health:',wild_pokemon['HP'])
        PythonGrammar.displayBlankLine()
        print('You have used:',user_attack['Name'])
        
        PythonGrammar.TimePause()
        
        #Calculating Damage
        dmg = BattleMechanics.Damage(user_attack,user_attack_multiplier)
        wild_pokemon['HP'] -= dmg
        user_attack['Count'] -= 1 #Reducing the attack counter. Example 20/20 becomes 19/20
        
        if wild_pokemon['HP'] < 0: #HP can't be -10
            wild_pokemon['HP'] = 0
        
        print('Damage on enemy',wild_pokemon['Name'],':',dmg)
        PythonGrammar.displayBlankLine()
        print('Wild',wild_pokemon['Name'],'health after',user_attack['Name'],':',wild_pokemon['HP'])
        
        if wild_pokemon['HP'] == 0: #Exiting the Loop if Opponent Pokemon HP<=0
            PythonGrammar.displayBlankLine()    
            print('Wild',wild_pokemon['Name'],'has fainted.')
            print('YOU WON!')
            PythonGrammar.displayBlankLine()
            PythonGrammar.displayLine()
            break
        
        PythonGrammar.TimePause()
    
        #NPC ATTACKING
        PythonGrammar.displayBlankLine()
        print(user_name,'\'s',user_pokemon['Name'],'health:',user_pokemon['HP'])
        PythonGrammar.displayBlankLine()
        print('Wild',wild_pokemon['Name'],'has used:',wild_attack['Name'])
        
        PythonGrammar.TimePause()
        
        #Calculating Damage
        dmg = BattleMechanics.Damage(wild_attack,wild_attack_multiplier)
        user_pokemon['HP'] -= dmg
        wild_attack['Count'] -= 1 #Reducing the attack counter. Example 20/20 becomes 19/20

        if user_pokemon['HP'] < 0: #HP can't be -10
            user_pokemon['HP'] = 0        

        print('Damage on your',user_pokemon['Name'],':',dmg)
        PythonGrammar.displayBlankLine()
        print('Your',user_pokemon['Name'],'health after',wild_attack['Name'],':',user_pokemon['HP'])
        PythonGrammar.displayBlankLine()
        
        if user_pokemon['HP'] == 0: #Exiting the Loop if User Pokemon HP<=0
            PythonGrammar.displayBlankLine()
            print('Your',user_pokemon,'has fainted.')
            print('YOU LOST.!')
            PythonGrammar.displayBlankLine()
            PythonGrammar.displayLine()
            break
        
        PythonGrammar.TimePause()
        
        #Giving User the Option to Capture WILD Pokemon
        if WildPokemonCapture.Choice(wild_pokemon) == True:
            
            capture = WildPokemonCapture.CaptureMain(user_details, wild_pokemon)
            if capture == True:
                break
            elif capture == False:
                continue
        
        else:
            pass
        
        #CONTINUE OR ESCAPE the Battle
        exits = ReadyConfirmExits.Exits()
        if exits == True:
            PythonGrammar.Loading('Escaping')
            break
        else:
            PythonGrammar.Loading('Continuing')
            continue
    
    PokemonMechanisms.giveXP(user_details,win)
    
    if PokemonCenter.choice() == True:
        PokemonCenter.use(user_details)
    
    return


def EncounterVillager(user_details):
    
    #Getting Villager Details
    villager_details = Villager.getVillager()()
    
    #Displaying Encounter
    Villager.displayEncounter(user_details, villager_details)
    
    #Rock Paper Scissors Mini-Game Choice: Do you want to play?
    choice = RockPaperScissorsVillager.Choice(villager_details)
    
    win = False
    if choice == True:
        win = RockPaperScissorsVillager.play(user_details,villager_details)
    else:
        pass
    
    if win == True:
        Item.giveItem(user_details,villager_details)
        #Using Item Given By Villager
        Item.useItem(user_details)
    
    else:
        print('You were unable to win the item:',villager_details['Item'])
        if RockPaperScissorsVillager.playagain(user_details) == True:
            EncounterVillager(user_details)
        else:
            pass
    
    return









#TOP-LEVEL STATEMENT
MainFunction()
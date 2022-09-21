import PythonGrammar

def displayEncounter(user_details,villager_details):
    
    PythonGrammar.displayBlankLine()
    print(user_details['Name'],'was walking peacefully when suddenly',villager_details['Name'],'appears before him!')
    
    PythonGrammar.Loading('Encountering A Villager')
    
    print(villager_details['Name'],': HI! I am',villager_details['Name'])
    print(villager_details['Name'],':','Do you want to play a game of Rock, Paper, Scissors with me?')
    print(villager_details['Name'],':','If you win, I will give you a valuable item.')
    
    PythonGrammar.Loading(villager_details['Name']+' is searching his pocket')
    
    print(villager_details['Name'],':','I will reward you with',villager_details['Item'])
    
    PythonGrammar.TimePause()
    
    return
    
def VillagerDetails():
    
    #Villager Info Dictionary
    villager_dic={}
    
    #Villager Tina
    villager_dic[1]={}
    villager_dic[1]['Name'] = 'Villager Tina'
    villager_dic[1]['Item'] = 'HP Potion' #Heals 10% of HP
    
    #Villager Mike
    villager_dic[2]={}
    villager_dic[2]['Name'] = 'Villager Mike'
    villager_dic[2]['Item'] = 'Attack Boost'
    
    return villager_dic #Returns entire Dictionary of all Villagers

def getVillager():
     
    #Fetching Random Villager
    import random
    n = random.randint(1,2)
    villager_dic = VillagerDetails()
    villager_details = villager_dic[n]
    
    return villager_details #Returns Villagers Details: Name, Item
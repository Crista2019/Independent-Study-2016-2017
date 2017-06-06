import random

def help():
  print("         ##     ## ######## ##       ########  ")
  print("         ##     ## ##       ##       ##     ##")
  print("         ##     ## ##       ##       ##     ## ")
  print("         ######### ######   ##       ########  ")
  print("         ##     ## ##       ##       ##        ")
  print("         ##     ## ##       ##       ##        ")
  print("         ##     ## ######## ######## ##        ")
  print('\n')
  print("Welcome to the help menu.")
  print("List of useful functions/methods to call and navigate this tool!:")
  print('\n')
  
  print("list_classes():", '\n', 'Fuction; Lists all possible classes that can be used in a typical D&D character.')
  
  print('\n')
  
  print("list_races():", '\n', "Function; Lists all possible races that can be used in a typical D&D character. ")
  
  print('\n')
  
  print('displayPartyMembers():', '\n', "Function; Prints all current members of a party. ")
  
  print('\n')
  
  print("printAllMaps():", '\n', "Function; prints all maps that have been created since the initializing the program.")
      
  print('\n')
  
  print("createNewPlayer():", '\n', "Function; One of the most useful tools to create a new player step by step.")
  
  print('\n')
  
  print("createNewMap():", '\n', "Function; Interactive step-by-step map maker")
  
  print('\n')
  
  
  
  print("createNewCampain():", '\n', "Function; Create a campaign by adding potential quest branches that emulate a 'choose your own adventure' style structure, primarily to assist the dungeon master through DMing")
  
  print('\n')
  
  print("Player(object):", '\n', "Class; contains data and methods for defining each player in a party.(PRIMARY DATA STRUCTURE: HASH MAP)")
  
  print('\n')
  
  print("Map(object):", '\n', "Class; contains basic map information as well as all the villages and connecting villages of a given map and methods for manipulating this data. (PRIMARY DATA STRUCTURE: GRAPH) ")
  
  print('\n')
  
  print("Quest(object):", '\n', "Class; contains methods (PRIMARY DATA STRUCTURE: BINARY TREE)")
  
  print('\n')
  
  print("", '\n', "")
  
  
  
  
  
  
  
  
  
  
  

possible_classes = ["barbarian", "bard", "cleric", "druid", "fighter", "mage", "monk", "paladin", "ranger", "sorcerer", "rogue", "warlock"]

def list_classes():
	print(possible_classes)

possible_races = ["human", "elf", "dwarf", "halfling", "gnome", "half-orc"]

def list_races():
	print(possible_races)
	
players = []

def playerIcon1():
  print('\n')
  print("        ,.,")
  print("       ((())")
  print("      (|*_*|)")
  print("       c\=/c")
  print('\n')
  
def playerIcon2():
  print('\n')
  print("      .-.")
  print("     (~ ~)")
  print("     :o o:")
  print("    (((_)))")
  print("      '-'")
  print('\n')
  
def playerIcon3():
  print('\n')
  print("       ,")
  print("   ,.'` `'.,")
  print("    |:o o:|")
  print("     \(_)/")
  print('\n')
  
def playerIcon4():
  print('\n')
  print("       ,")
  print("   ,.'` `'.,")
  print("    |:o o:|")
  print("     \(_)/")
  print('\n')
      
def playerIcon5():
  print("       ,")
  print("     ,iIi,")
  print("    (((()))")
  print("    ))o_o((")
  print("     '\=/'")
  print('\n')
      
def playerIcon6():
  print('\n')
  print("      ,.,")
  print("    ((~'~))")
  print("   '(|o_o|)'")
  print("   ,..\=/..,")
  print('\n')
      
def playerIcon7():
  print('\n')
  print("    (\___/)")
  print("     )o o(")
  print("    (_(_)_)")
  print('\n')
      
def playerIcon8():
  print('\n')
  print("    (@@@@@)")
  print("    @)0 0(@")
  print("    @((_))@")
  print("      )=(")
  print('\n')
      
def playerIcon9():
  print('\n')
  print("      ~I~")
  print("     ('¯`)")
  print("     )Ø Ø(")
  print("    ( (_) )")
  print("     `'-'`")
  print('\n')
      
def playerIcon10():
  print('\n')
  print("      ,.,")
  print("     (~ ~)")
  print("    q:0 0:p")
  print("     ((_))")
  print("      'u'")
  print('\n')

icons = (playerIcon1, playerIcon2, playerIcon3, playerIcon4, playerIcon5, playerIcon6, playerIcon7, playerIcon8, playerIcon9, playerIcon10)

maps = []

campaigns = []
campaign_names = {}

def printAllMaps():
  for x in range(0, len(maps)):
    print(maps[x].name)

def displayPartyMembers():
  print("Party:")
  for x in range(0, len(players)):
    print(players[x].name,)
  print("Party size: {}".format(Player.teamCount))
  
def printAllCampaigns():
  for x in range(0, len(campaign_names)):
    print(campaign_names[x])

def createNewPlayer():
  if input("Do you wish to create a new player? (y/n)").lower() == 'y':
    print("New player request granted.")
    
    print('\n')
    name = input("What is the the new character's name?")
    if name in players:
      print("Sorry, that name is taken. Please choose a name not already present within your party.")
      name = input("What is the the new character's name?")
    
    print("  _____")
    print(" /\ ' .\    ______")
    print("/: \____\  / .   /\ ")
    print("\ '/ .  / /_____/..\ ")
    print(" \/____/  \ ' ' \  / ")
    print("           \_'_'_\/")
    print('\n')
    
    n = len(players)
    players.append(Player(name))
    print('\n')
    players[n].init_inventory()
    print('\n')
    players[n-1].displayCharacter()
    
    print(name, " will be refered to as players[{}]".format(n))
    print("At any time, call players[number].displayCharacter() to check a player's stats. Make sure to start at 0!")
  else:
    print("Ok. New player request terminated")
  
def createNewMap():
  if input("Do you wish to create a new map? (y/n)").lower() == 'y':
    print("New map request granted.")
    
    print("            ___,")
    print("       _.-'` __|__")
    print("     .'  ,-:` \;',`'-,")
    print("    /  .'-;_,;  ':-;_,'.")
    print("   /  /;   '/    ,  _`.-\ ")
    print("   /  /;   '/    ,  _`.-\ ")
    print("  |  |:.  `\`-.   \_   / |")
    print("  |  |     (   `,  .`\ ;'|")
    print("   \  \     | .'     `-'/")
    print("    \  `.   ;/        .'")
    print("     '._ `'-._____.-'`")
    print("        `-.____|")
    print("          _____|_____")
    print("         /___________\ ")
    
    map_name = input("What would you like to call this new map?")
    what = input("What type of map is {}? (e.g. city, world, dungeon, etc)".format(map_name))
    
    m = len(maps)
    maps.append(Map(map_name, what))
    print(map_name, "will be refered to as maps[{}].".format(m))
    
    print('\n')
    maps[m].init_add_stops()
    
    print('\n')
    maps[m].printMap()
    
    print('\n')
    print("By default, the map is initialized in the 'unlocked' setting. To change this, call maps[number].lockMap() or maps[number].unlockMap()")
    
    print('\n')
    print("To add additional stops at any time, call maps[number].addStop('town name', 'connecting town name')")
    
    print("To learn information about a specific map, call maps[map number].printMap()")
    
    print('\n')
    print("To remove stops at any time, call maps[number].remove('town name')")
    
    print('\n')
    print("To print a working list of all maps, call printAllMaps()")
    
  else:
    print("Ok. New map request terminated.")
  
def createNewCampaign():
  if input("Do you wish to create a new campaign? (y/n)").lower() == 'y':
    print("New campaign request granted.")
    
    print("    ,-----------.")
    print("   (_\           \ ")
    print("      |           |")
    print("      |           |")
    print("      |           |")
    print("      |           |")
    print("     _|           |")
    print("    (_/_____(*)___/")
    print("             \ \ ")
    print("              ) ) ")
    print("              ^ ^")
    
    name = input("What shall the title of this campaign be?")
    root = input("What is the inciting incident of the campaign?")
    
    value1 = input("What is one possible quest that branches from this incident?")
    value2 = input("What is another possible quest that branches from this incident?")
    
    l = len(campaigns)
    campaign_names[Quest(root)]: campaign
    campaigns.append(Quest(root))
    
    campaigns[l].insert_left(value1)
    campaigns[l].insert_right(value2)
    
    if input("Do you have any further quests to add at this time? (y/n)") == 'y':
      add_quest = True
      
      while add_quest:
        value1a = input("What is one resulting quest from '{}'?".format(value1))
        campaigns[l].left_choice.insert_left(value1a)
        
        value1b = input("what is the second possible quest to choose resulting from '{}'?".format(value1))
        campaigns[l].left_choice.insert_right(value1b)
        
        value2a = input("Now, what is one resulting quest from '{}'?".format(value2))
        campaigns[l].right_choice.insert_left(value2a)
        
        value2b = input("what is the second possible quest to choose resulting from '{}'?".format(value2))
        campaigns[l].right_choice.insert_right(value2b)
        
        if input("Continue adding quests? (y/n)") =="y
          campaigns[l].left_choice.left_choice.insert_left(input("What is one resulting quest from '{}'?".format(value1a)))
          campaigns[l].left_choice.left_choice_choice.insert_right(input("what is the second possible quest to choose resulting from '{}'?".format(value1b)))
          
          campaigns[l].left_choice.right_choice.insert_left(input("What is one resulting quest from '{}'?".format(value2a)))
          campaigns[l].left_choice.right_choice.insert_right(input("what is the second possible quest to choose resulting from '{}'?".format(value2b)))
          add_quest = False
        else:
          add_quest = False
    print("Ok.", name, " has been created. Check the status of your quest progression by calling campaigns[number].print_quests(inciting incident)", "\n", "Change the quest order or continue adding new quests by calling campaigns[number].right_choice.insert_left('quest'), for example")
    print("\n")
    print("To print all existing campaigns, call printAllCampaigns()")
  else:
    print("Ok. New campaign request terminated.")

class Player(object):
		'Common base class for all players'
		teamCount = 0

		def __init__(self, name):

		  self.name = name #Primitive Data Structure: String
		  
		  self.race = input("Choose your race. (human, elf, dwarf, halfling, gnome, half-orc)").lower()
		  
		  #self.icon = input("Choose one of ten player icons [playerIcon1(), playerIcon6(), etc]")
		  
		  if self.race not in possible_races:
		    self.race = input("Please choose a valid race.")
		    
		  self.character_class = input("Choose your class. (barbarian, bard, cleric, druid, fighter, mage, monk, paladin, ranger, sorcerer, rogue, warlock)").lower()
		  
		  if self.character_class not in possible_classes:
		    self.character_class = input("Please choose a valid class.")
		    
		  self.stats = {"Strength": random.randint(3,18), "Constitution": random.randint(3,18), "Dexterity": random.randint(3,18), "Intelligence": random.randint(3,18), "Wisdom": random.randint(3,18), "Charisma": random.randint(3,18)}
		  
		  self.icon = icons[random.randint(0,9)]
		  
		  Player.teamCount += 1
		  self.inventory = set()
		
		def init_inventory(self):
		  if input("Do you wish to add any initial items to the inventory? (y/n)") == 'y':
		    addItems = True
		    while addItems:
		      self.addItemToInventory(input("What item should be added?"))
		      if input("Continue adding items to inventory? (y/n)") == 'n':
		        addItems = False
            
		def addItemToInventory(self, item):
			self.inventory.add(item)
    	
		def checkForItem(self,item):
			if item in self.inventory:
				return True
			else:
				print(item, " is not in ", self.name, "'s inventory.")

		def displayInventory(self):
		  print("Inventory items: {}".format(self.inventory) )

		def displayCharacter(self):
			print("Name : ", self.name)
			print("Statistics: ", self.stats)
			self.displayInventory()
			print("Class: ", self.character_class)
			print("Race: ", self.race)
			print("\n")
			displayPartyMembers()
			return self.icon()
		

#http://www.python-course.eu/python3_inheritance.php FOR ADDING DIFFERENT PLAYER CLASSES AND RACES IF TIME ALLOWS

"""
TODO:
1) Create a world or dungeon map using a graph (nodes/locations connected by edges with weights that represent distance and expended energy when crossing)...
2) A collection of quests using a tree (that way, even though there is still an order to which quests you can complete first, the players are still given a CYOA-esque choice)...
3. Linked list (potentially a queue) of different bosses or NPC (nonplayer characters) that you can create in a specific order that reflects leveling up (you may only reach the next one by going through the previous one)...
4. A history of the most recent boss, town, etc you have encountered using a stack
"""

class Map(object):
  """ Graph data structure, undirected by default. """
  mapCount = 0 
  
  def __init__(self, name, what, directed=False, locked=False): 
    #what refers to whether the map is of the game world, dungeon, room, etc
    #connections refers to the connection between nodes
    self.name = name
    self.what = what
    self.stops = {}
    #Will look like {('Town A': 'Town B'), ('Town B', 'Town C'), etc...}
    #A SET of DICTIONARIES in which each value in the key is the town name and the value is the conecting town
    self._directed = directed
    self.locked = bool(locked)
    
    Map.mapCount += 1

    #HERE IS WHERE I WILL ADD THE NODES THAT REPRESENT DIFFERENT VISITABLE LOCATION WITHIN THE MAP, AS WELL AS EDGES
    #THIS IS GOING TO BE IN THE FORM OF A UNDIRECTED, WEIGHTED GRAPH!
  def unlockMap(self):
    self.locked = False

  def lockMap(self):
    self.locked = True
  
  def printMap(self):
    print(self.name, " is a ", self.what, " map.")
    if self.locked:
      print("It is currently locked.")
    else:
      print("It is currently unlocked.")
    print(self.stops)

  def init_add_stops(self):
    if input("Would you like to add a new stop to {}? (y/n)".format(self.name)) == 'y':
        add_stops = True
        while add_stops:
          town = input("What is the name of this stop?")
          connecting_town = input("What town is {} connected to?".format(town))
          self.addStop(town, connecting_town)
          if input("Would you like to add another stop? (y/n)") == 'n':
            add_stops = False
  
  def addStop(self, town, connecting_town): 
    #"stop" input should be in the form of a TUPLE then will be turned into a DICTIONARY; stop = (town, connecting_town) then code => {town: connecting_town}
    if self.locked == False:
      self.stops[town] = connecting_town
      print("Modified map of", self.name, self.stops)
    else:
      print("The", self.name, "is LOCKED. DM must unlock this map by calling maps[map numer].unlockMap() to access it!")

  def remove(self, node):
    if self.locked != False:
      print("The", self.name, "is LOCKED. DM must reset the value of self.locked to True to unlock!")
    else:
      if node in self.stops: 
        del self.stops[node]

class Quest(object):
  #binary tree
  def __init__(self, val):
      self.left_choice = None
      self.right_choice = None
      self.data = val

  def insert_left(self, val):
    self.left_choice = Quest(val)
    return self.left_choice
    
  def insert_right(self, val):
    self.right_choice = Quest(val)
    return self.right_choice
    
  def __str__(self):
    return "{}({}, {})".format(self.val, self.left_choice, self.right_choice)
  
  def print_quests(self, val):
    print(val)
    self.print_quests(self.data.left_choice)
    self.print_quests(self.data.right_choice)
    
"""
me = Player("Crista")
me.addItemToInventory("thing")
me.checkForItem("thing")
me.displayCharacter()
"""
print("Welcome to Crista Falk's 'Dungeons and Dragons Python Interactive Gameplay Tool!'")
print("At any point in the game, for assistance with commands, simply type help() into the Python prompt.")
print("Why don't you start by creating a player, map, or campaign by calling createNewPlayer(), etc?")

print("                                               _   __,----'~~~~~~~~~`-----.__")
print("                                        .  .    `//====-              ____,-'~`")
print("                        -.            \_|// .   /||\ \  `~~~~`---.___./")
print("                  ______-==.       _-~o  `\/    |||  \ \           _,'`")
print("            __,--'   ,=='||\=_    ;_,_,/ _-'|-   |`\   \ \        ,'")
print("         _-'      ,='    | \ \`.    '',/~7  /-   /  ||   `\.     /")
print("       .'       ,'       |  \ \  \_  '' /  /-   /   ||      \   /")
print("      / _____  /         |   \ \.`-____/  /|- _/   ,||       \ /")
print("     ,-'     `-|--'~~`--_ \     `==-/  `|\ '--===-'       _/`")
print("               '         `-|      /|    )-'\~'      _,--''")
print("                           '-~^\_/ |    |   `\_   ,^             /\ ")
print("                                /  \     \__   \/~               `\__")
print("                            _,-' _/'\ ,-'~____-'`-/                 ``===\ ")
print("                           ((->/'    \|||' `.     `\.  ,                _||")
print("             ./                       \_     `\      `~---|__i__i__\--~'_/ ")
print("            <_n_                     __-^-_    `)  \-.______________,-~' ")
print("             `B'\)                  ///,-'~`__--^-  |-------~~~~^' ")
print("             /^>                           ///,--~`-\ ")
print("            `  `                                     ")


"""
class BinaryTree(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
   
  def insert_left(self, val):
    self.left = BinaryTree(val)
    
  def insert_right(self, val):
    self.right = BinaryTree(val)
  
  def __str__(self):
    return "{}({}, {})".format(self.val, self.left, self.right)
    
tree = BinaryTree("Animals")
tree.insert_left("Dog")
tree.insert_right("Cat")
tree.left.insert_left("Shnouzer")
tree.left.insert_right("Poodle")
tree.left.right.insert_left("Golden Doodlie thing.")
print tree.left.right.left.val
              Animals
              /    \
            Dog     Cat
           /   \
     Shnouzer  Poodle
                /
          Golden Doodlie Thing
print tree #Expect "Animals(Dog( ... ), Cat(None, None))
"""

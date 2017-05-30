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
  print("")

possible_classes = ["barbarian", "bard", "cleric", "druid", "fighter", "mage", "monk", "paladin", "ranger", "sorcerer", "rogue", "warlock"]

def list_classes():
	print(possible_classes)

possible_races = ["human", "elf", "dwarf", "halfling", "gnome", "half-orc"]

def list_races():
	print(possible_races)
	
max_players = ["player1", "player2", "player3", "player4", "player5", "player6", "player7", "player8", "player9", "player10"]

def displayPartyMembers():
  print("Party:", Player.teamList, "(Party size: {})".format(Player.teamCount))

def createNewPlayer():
  if input("Do you wish to create a new player? (y/n)").lower() == 'y':
    print("New player request granted.")
    
    print('\n')
    name = input("What is the the new character's name?")
    if name in Player.teamList.keys():
      print("Sorry, that name is taken. Please choose a name not already present within your party.")
      name = input("What is the the new character's name?")
    
    print("  _____")
    print(" /\ ' .\    ______")
    print("/: \____\  / .   /\ ")
    print("\ '/ .  / /_____/..\ ")
    print(" \/____/  \ ' ' \  / ")
    print("           \_'_'_\/")
    print('\n')
    
    n = Player.teamCount
    if n == 0:
      player1 = Player(name)
      player1.init_inventory()
      print('\n')
      print(name, " will be refered to as player1.")
      
      print('\n')
      print("        ,.,")
      print("       ((())")
      print("      (|*_*|)")
      print("       c\=/c")
      print('\n')
      
      player1.displayCharacter()
    elif n == 1:
      player2 = Player(name)
      player2.init_inventory()
      print('\n')
      print(name, " will be refered to as player2.")
      
      print('\n')
      print("      .-.")
      print("     (~ ~)")
      print("     :o o:")
      print("    (((_)))")
      print("      '-'")
      print('\n')
      
      player2.displayCharacter()
    elif n == 2:
      player3 = Player(name)
      player3.init_inventory()
      print('\n')
      print(name, " will be refered to as player3.")
      print('\n')
      print("       ,")
      print("   ,.'` `'.,")
      print("    |:o o:|")
      print("     \(_)/")
      print('\n')
      player3.displayCharacter()
    elif n == 3:
      player4 = Player(name)
      player4.init_inventory()
      print('\n')
      print(name, " will be refered to as player4.")
      print('\n')
      print("       ,")
      print("     ,iIi,")
      print("    (((()))")
      print("    ))o_o((")
      print("     '\=/'")
      print('\n')
      player4.displayCharacter()
    elif n == 4:
      player5 = Player(name)
      player5.init_inventory()
      print('\n')
      print(name, " will be refered to as player5.")
      print('\n')
      print("      ,.,")
      print("    ((~'~))")
      print("   '(|o_o|)'")
      print("   ,..\=/..,")
      print('\n')
      player5.displayCharacter()
    elif n == 5:
      player6 = Player(name)
      player6.init_inventory()
      print('\n')
      print(name, " will be refered to as player6.")
      print('\n')
      print("    (\___/)")
      print("     )o o(")
      print("    (_(_)_)")
      print('\n')
      player6.displayCharacter()
    elif n == 6:
      player7 = Player(name)
      player7.init_inventory()
      print('\n')
      print(name, " will be refered to as player7.")
      print('\n')
      print("    (@@@@@)")
      print("    @)0 0(@")
      print("    @((_))@")
      print("      )=(")
      print('\n')
      player7.displayCharacter()
    elif n == 7:
      player8 = Player(name)
      player8.init_inventory()
      print('\n')
      print(name, " will be refered to as player8.")
      print('\n')
      print("      ~I~")
      print("     ('¯`)")
      print("     )Ø Ø(")
      print("    ( (_) )")
      print("     `'-'`")
      print('\n')
      player8.displayCharacter()
    elif n == 8:
      player9 = Player(name)
      player9.init_inventory()
      print('\n')
      print(name, " will be refered to as player9.")
      print('\n')
      print("      ,.,")
      print("     ((())")
      print("    (|o_o|)")
      print("    ()\=/()")
      print("    ()\_/()")
      print('\n')
      player9.displayCharacter()
    elif n == 9:
      player10 = Player(name)
      player10.init_inventory()
      print('\n')
      print(name, " will be refered to as player10.")
      print('\n')
      print("      ,.,")
      print("     (~ ~)")
      print("    q:0 0:p")
      print("     ((_))")
      print("      'u'")
      print('\n')
      player10.displayCharacter()
    else:
      print("The party has exceeded the max amount of manageable players. No more than ten people per campain.")
    print('\n')
    print("At any time, call player[number].displayCharacter() to check your player's stats.")

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
    
  else:
    print("Ok. New map request terminated.")
  
def createNewCampain():
  if input("Do you wish to create a new campain? (y/n)").lower() == 'y':
    print("New campain request granted.")
    
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
    
  else:
    print("Ok. New campain request terminated.")

class Player(object):
		'Common base class for all players'
		teamCount = 0
		teamList = {}

		def __init__(self, name):

		  self.name = name #Primitive Data Structure: String
		  
		  self.race = input("Choose your race. (human, elf, dwarf, halfling, gnome, half-orc)").lower()
		  
		  if self.race not in possible_races:
		    self.race = input("Please choose a valid race.")
		    
		  self.character_class = input("Choose your class. (barbarian, bard, cleric, druid, fighter, mage, monk, paladin, ranger, sorcerer, rogue, warlock)").lower()
		  
		  if self.character_class not in possible_classes:
		    self.character_class = input("Please choose a valid class.")
		    
		  self.stats = {"Strength": random.randint(3,18), "Constitution": random.randint(3,18), "Dexterity": random.randint(3,18), "Intelligence": random.randint(3,18), "Wisdom": random.randint(3,18), "Charisma": random.randint(3,18)}
			
		  Player.teamList[self.name] = max_players[Player.teamCount]
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
			print("Member of party:", Player.teamList, "(Party size: {})".format(Player.teamCount))
		

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

    #HERE IS WHERE I WILL ADD THE NODES THAT REPRESENT DIFFERENT VISITABLE LOCATION WITHIN THE MAP, AS WELL AS EDGES
    #THIS IS GOING TO BE IN THE FORM OF A UNDIRECTED, WEIGHTED GRAPH!
  def unlockMap(self):
    self.locked = False

  def lockMap(self):
    self.locked = True

  def addStop(self, stop): 
    #"stop" input should be in the form of a TUPLE then will be turned into a DICTIONARY; stop = (town, connecting_town) then code => {town: connecting_town)
    if self.locked == False:
      for town, connecting_town in stop:
            self.stops[town] = connecting_town
      print("Modified map of", self.name, self.stops)
    else:
      print("The", self.name, "is LOCKED. DM must reset the value of self.locked to True to unlock!")

  def remove(self, node):
    if self.locked != False:
      print("The", self.name, "is LOCKED. DM must reset the value of self.locked to True to unlock!")
    else:
      for x in self.stops:
        if x == node:
          #NEXT STEP IS TO DELETE X IF IT IS FOUND
        #ELSEIF X == ONE OF THE VALUES RATHER THAN KEYS, DELETE CONNECTION
          pass
"""
  def is_connected(self, node1, node2):
    # Is node1 directly connected to node2
    return node1 in self._graph and node2 in self._graph[node1]

  def find_path(self, node1, node2, path=[]):
  #Find any path between node1 and node2 (may not be shortest) 

    path = path + [node1]
    if node1 == node2:
      return path
    if node1 not in self._graph:
      return None
    for node in self._graph[node1]:
      if node not in path:
          new_path = self.find_path(node, node2, path)
      if new_path:
        return new_path
      return None
"""

class Quest(object):
  #binary search tree
  def __init__(self, val):
      self.quest_choice_one = None
      self.quest_choice_two = None
      self.data = val

  def binary_insert(self, root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.quest_choice_one is None:
                root.quest_choice_one = node
            else:
                self.binary_insert(root.quest_choice_one, node)
        else:
            if root.quest_choice_two is None:
                root.quest_choice_two = node
            else:
                self.binary_insert(root.quest_choice_two, node)
  
  def print_quests(self, root):
    if not root:
        return        
    print(root.data)
    self.print_quests(root.quest_choice_one)
    self.print_quests(root.quest_choice_two)   
    
"""
me = Player("Crista")
me.addItemToInventory("thing")
me.checkForItem("thing")
me.displayCharacter()
"""
print("Welcome to Crista Falk's 'Dungeons and Dragons Python Interactive Gameplay Tool!'")
print("At any point in the game, for assistance with commands, simply type help() into the Python prompt.")
print("Why don't you start by creating a player, map, or campain by calling createNewPlayer(), etc?")

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

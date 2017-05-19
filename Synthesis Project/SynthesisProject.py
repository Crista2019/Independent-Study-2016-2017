import random
#import Image
# ^^^ I WILL CONSIDER ADDING CHARATER SPRITES ONCE I FINISH TASKS WITH HIGHER PRIORITIES
possible_classes = ["barbarian", "bard", "cleric", "druid", "fighter", "mage", "monk", "paladin", "ranger", "sorcerer", "rogue", "warlock"]
def list_classes():
	print(possible_classes)

possible_races = ["human", "elf", "dwarf", "halfling", "gnome", "half-orc"]
def list_races():
	print(possible_races)

class Player(object):
		'Common base class for all players'
		teamCount = 0
		teamList = []


		def __init__(self, name): #, image):
			self.name = name #Primitive Data Structure: String

			self.race = input("Choose your race.").lower()
			if self.race not in possible_races:
				self.race = input("Please choose a valid race. Call list_races() for help. Then redefine self.race as a valid option.")

			self.character_class = input("Choose your class.").lower()
			if self.character_class not in possible_classes:
				self.character_class = input("Please choose a valid class. Call list_classes() for help. Then redefine self.character_class as a valid option.")


			self.stats = {"Strength": random.randint(3,18), "Constitution": random.randint(3,18), "Dexterity": random.randint(3,18), "Intelligence": random.randint(3,18), "Wisdom": random.randint(3,18), "Charisma": random.randint(3,18)}
			Player.teamCount += 1
			self.teamList.append(self.name)
			self.inventory = set()
			#self.characterSprite = image #Image in the form of image.jpg

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
			print(", Statistics: ", self.stats)
			#Image.open(self.characterSprite)
			#self.characterSprite.show()

#http://www.python-course.eu/python3_inheritance.php FOR ADDING DIFFERENT PLAYER CLASSES AND RACES IF TIME ALLOWS

""" TODO:
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
  def addStop(self, stop): 
    #"stop" input should be in the form of a TUPLE then will be turned into a DICTIONARY; stop = (town, connecting_town) then code => {town: connecting_town)
    if self.locked == False:
      for town, connecting_town in stop:
            self.stops[town] = connecting_town
      print("Modified map of", self.name, self.stops)
    else:
      print("The", self.name, "is LOCKED. DM must reset the value of self.locked to True to unlock!")

  def remove(self, node):
    if self.locked == False:
      for x in self.stops:
        if x == node:
          #NEXT STEP IS TO DELETE X IF IT IS FOUND
        #ELSEIF X == ONE OF THE VALUES RATHER THAN KEYS, DELETE CONNECTION
    else:
      print("The", self.name, "is LOCKED. DM must reset the value of self.locked to True to unlock!")
      
  def is_connected(self, node1, node2):
    """ Is node1 directly connected to node2 """
    return node1 in self._graph and node2 in self._graph[node1]

  def find_path(self, node1, node2, path=[]):
    """ Find any path between node1 and node2 (may not be shortest) """

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

  def unlockMap(self):
    self.locked = False

  def lockMap(self):
    self.locked = True

"""
class Quest(object):
	def __init__(self, campaign_name):
	  """

me = Player("Crista")
me.addItemToInventory("thing")
me.checkForItem("thing")
me.displayCharacter()

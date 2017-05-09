import random
#import Image 
# ^^^ I WILL CONSIDER ADDING CHARATER SPRITES ONCE I FINISH TASKS WITH HIGHER PRIORITIES

class Player:
		'Common base class for all players'
		teamCount = 0

		def __init__(self, name): #, image):
			self.name = name #Primitive Data Structure: String
			self.stats = {"Strength": random.randint(3,18), "Constitution": random.randint(3,18), "Dexterity": random.randint(3,18), "Intelligence": random.randint(3,18), "Wisdom": random.randint(3,18), "Charisma": random.randint(3,18)}
			Player.teamCount += 1
			self.inventory = set()
			#self.characterSprite = image #Image in the form of image.jpa
      
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

class Map:
  def __init__(self, name, what, locked): #what refers to whether the map is of the game world, dungeon, room, etc
    self.name = name
    self.what = what
    self.locked = bool(locked)
    #HERE IS WHERE I WILL ADD THE NODES THAT REPRESENT DIFFERENT VISITABLE LOCATION WITHIN THE MAP, AS WELL AS EDGES 
    #THIS IS GOING TO BE IN THE FORM OF A UNDIRECTED, WEIGHTED GRAPH!
    
  def unlockMap(self):
    self.locked = False
    
  def lockMap(self):
    self.locked = True
    


me = Player("Crista", "ws_Graphic_Art_Bug_1920x1080.jpg")
me.addItemToInventory("thing")
me.checkForItem("thing")
me.displayCharacter()

#This is a data strcture implentation of the MAX binary heap ADT
class BinaryHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def buildHeap(self,theList):
		midItem = len(theList) // 2
		self.currentSize = len(theList)
		self.heapList = [0] + theList[:]
		#This sorts through the priority queue/max heap and sorts through the data (starting at the middle) to reposition the greatest key values in order at the front
		while (midItem > 0):
			self.percUp(item)
			midItem -= 1

	def percUp(self, insertedItem):
		#Ensuring that the data structure remains a BINARY heap w/ 2 branches at most
		while insertedItem // 2 > 0:
			#If the new key value is greater than its parent..
			if self.heapList[insertedItem] > self.heapList[insertedItem // 2]:
				temp = self.heapList[insertedItem // 2]
				#The root node and the inserted value will swap places (i.e. percolate)
				self.heapList[insertedItem // 2] = self.heapList[insertedItem]
				self.heapList[insertedItem] = temp
			insertedItem = insertedItem // 2

	def insert(self, item):
		self.heapList.push(item)
		self.currentSize += 1
		#Maintaining heap order property, so the child item will be LESS than its parent node
		self.percolate(self.currentSize)

	#This is easy because the last, least prioritized item is always the list in the last
	def delMin(self):
		self.heapList.pop()

	#This requires the deletion of the node item (i.e. the greatest value)
	#The second step in to percolate down in order to maintain heap order property. 
	#The second greatest value after the removed item will move to the front, and all other values stemming from the NEW node will shift forward, esuring that the heap retains structure.
	def percDown(self, newFront):
		while (newFront * 2) <= self.currentSize:
			maCh = self.maxChild(newFront)
			#If the item that has replaced the removed head is less than its child, they need to be switched
			if self.heapList[newFront] < self.heapList[maCh]:
				temp = self.heapList[newFront]
				self.heapList[newFront] = self.heapList[maCh]
				self.heapList[maCh] = temp
			newFront = maCh

	def maxChild(self, replacedFront):
		#Finding which of the children nodes has the greatest value then returning that for the percolating methd to use
		if (replacedFront * 2) + 1 < self.currentSize:
			return replacedFront * 2
		else:
			if self.heapList[replacedFront * 2] > self.heapList[replacedFront * 2 + 1]:
				return i * 2
			else:
				return replacedFront * 2 + 1

	def delMax(self):
		removedVal = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize -= 1
		self.heapList.pop()
		self.percDown(1)
		return removedVal

"""
COMPUTATIONAL COMPLEXITIES:
binary heap implementation

	enqueue and dequeue are both equal to O(log n)

	  insert  	  deleteMin    remove  	  findMin  
 	  O(log n)	  O(log n)	   O(log n)	  O(1)

"""

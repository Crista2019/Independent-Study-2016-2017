"""
Let's code up a represenation of a LinkedList.
	You can use whatever language you'd like, but use a Class to create the LinkedList as this will help you think of the problem in the right paradigm.
	Our LinkedList class should have a few methods,
	in addition to two constructors
	--one which accepts a value as the only parameter and the other which accepts a value and the LinkedList-to-follow as a second parameter
"""

print("In addition to the constructor described above, implement the following methods on your LinkedList class:")

#singly linked list data structure class
class LinkedList(object):
	def __init__(self, head, rest=None):
		self.head = head #first value which points to next value
		self.rest = rest #remainiing values in SLL

    #tells Python how to print the LL in which one value is only able to access the immediate next
	def __repr__(self):
		return "{} --> {}".format(self.head, self.rest)

    #example of recursion: when something is defined by type (itself).
    #Linked List is defined by being larger than at least one more value ahead of it
	def size(self):
		if self.rest:
			return 1 + self.rest.size()
		else:
			return 1

    #Append (insert at the end) a new value B into the Linked List.
		#my_linked_list.append(42) will add the integer 42 to the end of the list
	def append(self, val):
		if self.rest == None:
			self.rest = LinkedList(val)
		else: 
			self.rest.append(val)

    #Search to see if a value A is contained in the Linked List. (Note: it might not!)
		#my_linked_list.contains(42) will return true or false.
	def contains(self, val):
		if self.head == val:
			return True
		elif self.rest.contains(val):
			return True
		else:
			return False

    #Delete the i-th entry from the Linked List, where where 0 < i < n.
	    #my_linked_list.delete(1) will delete the second entry (the first is index=0).
	def delete(self, val):
		if self.rest:
			if val == 0:
				self.head = self.rest.head
				self.rest = self.rest.rest
			else:
				self.rest.delete(val-1)

    #Retrieve the i-th entry from the LinkedList, where 0 < i < n.
	    #my_linked_list.get(1) will return the value of the second entry.
	def get(self, index):
		if index == 0: 
			return self.head
		elif self.rest:
			return self.rest.get(index)
		else:
			return False
			raise Exception("This position is not contained in this list")
			

    #Prepend (insert at the beginning) a new value B into the Linked List.
	    #my_linked_list.preppend(42) will add the integer 42 to the start of the list.
	def prepend(self, val):
		new_liList = LinkedList(self.head, self.rest)
		self.head = val
		self.rest = new_liList


    #Insert a new value B into the Linked List at position i, where 0 < i < n.
	    #my_linked_list.insert(42) will add the integer 42 to the i-ith position in the list.
	def insert(self, pos, val):
		if pos == 0:
			self.prepend(val)
		elif self.rest:
			self.rest.insert(pos, val)
		else:
			raise Exception("This position is not contained in this list")

print("For the 6 methods described above, which are accessors and which are mutators?")

accessors = ["contains", "get"]
mutators = ["append", "delete", "prepend", "insert"]

print(accessors)
print(mutators)

print("Determine the computational complexity in 'Big O notation' of the using the following methods on the LinkedList object you implemented:")
comp = "Computational Complexity: "

list_1 = LinkedList("D")
list_2 = LinkedList("C", list_1)
list_3 = LinkedList("B", list_2)
test_list = LinkedList("A", list_3)

	#Search to see if a value A is contained in the Linked List. (Note: it might not!)
print(test_list)
test_list.contains("A")
print(comp + "O(n) where n = # of elements in the LL")

	#Delete the i-th entry from the Linked List, where where 0 < i < n.
test_list.delete(0)
print(test_list)
print(comp + "O(n) where n = # of elements in the LL")

	#Retrieve the i-th entry from the LinkedList, where 0 < i < n.
test_list.get(0)
print(comp + "O(n) where n = # of elements in the LL")

	#Prepend (insert at the beginning) a new value B into the Linked List.
test_list.prepend("AA")
print(test_list)
print(comp + "O(1) or O(c); CONSTANT")

	#Append (insert at the end) a new value B into the Linked List.
test_list.append("Z")
print(comp + " O(n) where n = # of elements in the LL")

	#Insert a new value B into the Linked List at position i, where 0 < i < n.
test_list.insert("E", 2)
print(comp + "O(n) where n = # of elements in the LL")

# A quick test suite that runs through each function. This *could* be more wholesome...
test_list = LinkedList(1)
test_list.prepend(2)
assert test_list.get(0) == 2
test_list.append(3)
assert test_list.get(2) == 3
assert test_list.contains(3)
test_list.append(4)
assert test_list.get(3) == 4
test_list.delete(2)
assert test_list.get(2) == 4
assert not test_list.contains(3)
test_list.insert(1, 5)
test_list.delete(0)
assert test_list.get(0) == 5
assert test_list.size() == 3
print("All tests pass! Woohoo!")

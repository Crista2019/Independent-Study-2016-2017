"""
Let's code up a represenation of a Array. 
	You can use whatever language you'd like, but use a Class to create the Array as this will help you think of the problem in the right paradigm. 
	Our Array class should have a few methods, 
	in addition to two constructors 
	--one which accepts a value as the only parameter and the other which accepts a value and the Array-to-follow as a second parameter
"""

print("In addition to the constructor described above, implement the following methods on your Array class:")

class Array(object):
    def __init__(self, new_list): #CASEY: "list" is actually a keyword in Python, so be wary of using it. Maybe "new_list" or "my_list" or something.
        self.new_list = new_list 

    #Append (insert at the end) a new value B into the Array.
		#my_linked_list.append(42) will add the integer 42 to the end of the list.
    def append(self, val):
        self.new_list[self.new_list.len()] = self.val

    #Search to see if a value A is contained in the Array. (Note: it might not!)
		#my_linked_list.contains(42) will return true or false.
    def contains(self, val): 
        for item in self.new_list: 
            if item == val: 
                return True
        return False 

    #Delete the i-th entry from the Array, where where 0 < i < n.
	    #my_linked_list.delete(1) will delete the second entry (the first is index=0).
    def delete(self, val):
        for i in range(self.new_list.len()):
            if i == val:
	        	del i

    #Retrieve the i-th entry from the Array, where 0 < i < n.
	    #my_linked_list.get(1) will return the value of the second entry.
    def get(self, i):
        return self.new_list[i]
            
    #Prepend (insert at the beginning) a new value B into the Array.
	    #my_linked_list.preppend(42) will add the integer 42 to the start of the list.
    def prepend(self, val):
        self.new_list = [val] + self.new_list
    
    #Insert a new value B into the Array at position i, where 0 < i < n.
	    #my_linked_list.insert(42) will add the integer 42 to the i-ith position in the list.
    def insert(self, val, pos):
        self.new_list = self.new_list[:pos] + [self.val] + self.new_list[pos+1:]

print("For the 6 methods described above, which are accessors and which are mutators?")

accessors = []
mutators = []

accessors.append("contains", "get")
mutators.append("append", "delete", "prepend", "insert")

print(accessors)
print(mutators)

print("Determine the computational complexity (in \"Big O\" notation) of the using the following methods on the Array object you implemented:")

comp = "Computational Complexity: "
testList = Array(["A", "B", "C", "D", 5, 6, 7])
otherList = Array(["aye", "bee", "see", "dee"])

	#Search to see if a value A is contained in the Array. (Note: it might not!)
print(testArray)
testArray.self.contains("A", self)
print(comp + "(O)N: 1 for first (0th) index, or (i + 1) when i is the index of the searched value, which varies")

print(otherArray)
otherArray.self.contains("A", self)
print(comp + "(O)N: 4, or new_list.len() because this new_list does not contain the value")

	#Delete the i-th entry from the Array, where where 0 < i < n.
testArray.self.delete(0, self)
print(testArray)
print(comp + "(O)N: 1 for first (0th) index, or (i + 1) when i is the index passed as a parameter of the .delete method")

	#Retrieve the i-th entry from the Array, where 0 < i < n.
testArray.get(0, self)
print(comp + "(O)1: 1 for the any index since each datum doesn't have to be accessed from a previous value like in the case of a linked new_list; it can just be referenced directly")

	#Prepend (insert at the beginning) a new value B into the Array.
testArray.prepend("AA", self)
print(testArray)
print(comp + "(O)1: simply redefining the list as an all-encompassing value and redefining the list to have two values, the new (0th index) value at the beginning and then cotents of the previous list")

	#Append (insert at the end) a new value B into the Array.
testArray.append("Z", self)
print(comp + "(O)1: see description for .prepend method")

	#Insert a new value B into the Array at position i, where 0 < i < n.
testArray.insert("E", self, 5, self)
print(comp + "(O)1: also redefining a value at a specific index, not searching through the existing values to do so")

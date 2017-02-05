"""
Let’s code up a represenation of a Array. 
	You can use whatever language you’d like, but use a Class to create the Array as this will help you think of the problem in the right paradigm. 
	Our Array class should have a few methods, 
	in addition to two constructors 
	--one which accepts a value as the only parameter and the other which accepts a value and the Array-to-follow as a second parameter
"""

print("In addition to the constructor described above, implement the following methods on your Array class:")

class Array(object):
    def __init__(self, List):
        self.list = list 

    #Append (insert at the end) a new value B into the Array.
		#my_linked_list.append(42) will add the integer 42 to the end of the list.
    def append(self, val, list):
        self.list[self.list.len()] = self.val
        return self.list

    #Search to see if a value A is contained in the Array. (Note: it might not!)
		#my_linked_list.contains(42) will return true or false.
    def contains(self, val, list):
        self.false = True
        for i in self.list:
            if self.list[i] == self.val:
                return True
                false = False
        if false == True:
            return False

    #Delete the i-th entry from the Array, where where 0 < i < n.
	    #my_linked_list.delete(1) will delete the second entry (the first is index=0).
    def delete(self, val, list):
        for i in self.list:
            while 0 < i and i < self.list.len():         
                if i == self.val:
                    del self.list[self.val]
        return self.list

    #Retrieve the i-th entry from the Array, where 0 < i < n.
	    #my_linked_list.get(1) will return the value of the second entry.
    def get(self, val, list):
        for i in self.list:
            while 0 < i and i < self.list.len():
                if i == self.val:
                    return self.list[self.val]
            
    #Prepend (insert at the beginning) a new value B into the Array.
	    #my_linked_list.preppend(42) will add the integer 42 to the start of the list.
    def prepend(self, val, list):
        for i in self.list:
            self.list[i] = self.list[i+1]
        self.list[0] = self.val
        return self.list
    
    #Insert a new value B into the Array at position i, where 0 < i < n.
	    #my_linked_list.insert(42) will add the integer 42 to the i-ith position in the list.
    def insert(self, val, pos, list):
        self.list[pos] = self.val 
        return self.list

print("For the 6 methods described above, which are accessors and which are mutators?")

accessors = []
mutators = []

accessors.append("contains", "get")
mutators.append("append", "delete", "prepend", "insert")

print(accessors)
print(mutators)

print("Determine the computational complexity (in “Big O” notation) of the using the following methods on the Array object you implemented:")

comp = "Computational Complexity: "
testList = Array(["A", "B", "C", "D", 5, 6, 7])
otherList = Array(["aye", "bee", "see", "dee"])

	#Search to see if a value A is contained in the Array. (Note: it might not!)
print(testArray)
testArray.self.contains("A", self)
print(comp + "1 for first (0th) index, or (i+1) when i is the index of the searched value, which varies")

print(otherArray)
otherArray.self.contains("A", self)
print(comp + "4, or list.len() because this list does not contain the value")

	#Delete the i-th entry from the Array, where where 0 < i < n.
testArray.self.delete(0, self)
print(testArray)
print(comp + "1 for first (0th) index, or (i + 1) when i is the index passed as a parameter of the .delete method")

	#Retrieve the i-th entry from the Array, where 0 < i < n.
testArray.get(0, self)
print(comp + "1 for the first index, or (i + 1) when i is the index passed as a parameter of the .get method")

	#Prepend (insert at the beginning) a new value B into the Array.
testArray.prepend("AA", self)
print(testArray)
print(comp + "8, equal to (n + 1) when n is the total number of seperate values in the list (i.e. list.len()")

	#Append (insert at the end) a new value B into the Array.
testArray.append("Z", self)
print(comp + "8, equal to (n + 1) when n is the total number of seperate values in the list (i.e. list.len()")

	#Insert a new value B into the Array at position i, where 0 < i < n.
testArray.insert("E", self, 5, self)
print(comp + "6 for the fifth index, or  (i + 1) when i is the index passed as a parameter of the .insert method")

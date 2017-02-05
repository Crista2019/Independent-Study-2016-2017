"""
Let's code up a represenation of a Array. 
	You can use whatever language you'd like, but use a Class to create the Array as this will help you think of the problem in the right paradigm. 
	Our Array class should have a few methods, 
	in addition to two constructors 
	--one which accepts a value as the only parameter and the other which accepts a value and the Array-to-follow as a second parameter
"""

print("In addition to the constructor described above, implement the following methods on your Array class:")

class Array(object):
    def __init__(self, list): #CASEY: "list" is actually a keyword in Python, so be wary of using it. Maybe "new_list" or "my_list" or something.
        self.list = list 

    #Append (insert at the end) a new value B into the Array.
		#my_linked_list.append(42) will add the integer 42 to the end of the list.
    def append(self, val): #CASEY: We never use that "list" variable, so we actually don't need it. We're using the "self.list" attribute instead.
        self.list[self.list.len()] = self.val
        #CASEY: If we want this to be a "mutator", we actually don't need to return the list itself. We've already changed "self", anyway.

    #Search to see if a value A is contained in the Array. (Note: it might not!)
		#my_linked_list.contains(42) will return true or false.
    def contains(self, val): # CASEY: We don't actually need that "list" variable -- so let's delete it. :-)
        #CASEY: Try to limit the number of variables you need, as often it will make your code cleaner.
        for item in self.list: #CASEY: Be careful what you're iterating over. In this case, "i" is not the index but the item itself.
            if item == val: #CASEY: Since we're iterating through items, we actually don't need to use the brackets.
                return True
        return False #CASEY: If we make it through the whole list without finding the "val", it logically can't have been there -- so return False.

    #Delete the i-th entry from the Array, where where 0 < i < n.
	    #my_linked_list.delete(1) will delete the second entry (the first is index=0).
    def delete(self, val):
        for i in range(self.list.len()): #CASEY: If we want to iterate through the indices, we'll need to create a "range".
            #CASEY: We're already iterating through the whole array, so no need to loop again with that "while" loop.
            if self.list[i] == val:
	        del self.list[i]
        # No need to return; this is a "mutator" after all.

    #Retrieve the i-th entry from the Array, where 0 < i < n.
	    #my_linked_list.get(1) will return the value of the second entry.
    def get(self, i):
        return self.list[i] #CASEY: The "get" method isn't as complicated with an ArrayList. Really, we can just defer to the "get" or "indexing" function of the Python list (stored at "self.list").
            
    #Prepend (insert at the beginning) a new value B into the Array.
	    #my_linked_list.preppend(42) will add the integer 42 to the start of the list.
    def prepend(self, val):
        # CASEY: Prepend doesn't necessarily "need" to loop through the list. Really, we just need to pop something on the front of the list.
        self.list = [val] + self.list
    
    #Insert a new value B into the Array at position i, where 0 < i < n.
	    #my_linked_list.insert(42) will add the integer 42 to the i-ith position in the list.
    def insert(self, val, pos):
        #CASEY: Super close, but we want to make sure we don't "erase" any data in the list. We just want to add/inject "more".
        self.list = self.list[:pos] + [self.val] + self.list[pos+1:]

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

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
		#my_linked_list.append(42) will add the integer 42 to the end of the list.
    def append(self, val):
        new_liList = LinkedList(self.head, self.rest)
        for i in new_liList: #CASEY: I don't think you need this `for` loop. Use `for` loops when you're doing stuff with multiple things; here, we're just doing *one* thing.
            if self.rest: #CASEY: What's this doing?
                pass
            else:
                self.head = new_liList
                self.rest = val

    #Search to see if a value A is contained in the Linked List. (Note: it might not!)
		#my_linked_list.contains(42) will return true or false.
    def contains(self, val):
        new_liList = LinkedList(self.head, self.rest)
		#CASEY: The tricky part here is just as you described it. Think *recursively*. I'll include a recursion helper assignment next lab.
        for item in new_liList: #This might be an inefficient/incorrect way of establishing this method, but I'm not sure how to search through nested list values when there is an N number of values contained in head/rest
            if self.head.size() > 0:
                for item in self.head:
                    if item == self.val:
                        return True
            if self.rest.size() > 0:
                for item in self.rest:
                    if item == self.val:
                        return True
            else:
                return False

    #Delete the i-th entry from the Linked List, where where 0 < i < n.
	    #my_linked_list.delete(1) will delete the second entry (the first is index=0).
    def delete(self, liList):
        for i in self.liList: #CASEY: You actually don't need `for` loops for these methods, nor `while` loops. You have a habit of using them; be careful as they can be "expensive". ;-)
            while 0 < i and i < self.liList.len():
                if i == self.val:
                    del self.liList[self.val]
        return self.liList

    #Retrieve the i-th entry from the LinkedList, where 0 < i < n.
	    #my_linked_list.get(1) will return the value of the second entry.
    def get(self, val):
        new_liList = LinkedList(self.head, self.rest)
        for i in new_liList: #CASEY: No `for` loops!
            if val == 0:
                return self.head
            else:
                for item in self.rest:
                    return new_liList[val] #Again, I am really just trying to visualize what the PROCESS should be; I doubt that any of these methods will resemble any sort of functioning code in execution XD

    #Prepend (insert at the beginning) a new value B into the Linked List.
	    #my_linked_list.preppend(42) will add the integer 42 to the start of the list.
    def prepend(self, val):
        new_liList = LinkedList(self.head, self.rest)
        self.head = val
        self.rest = new_liList


    #Insert a new value B into the Linked List at position i, where 0 < i < n.
	    #my_linked_list.insert(42) will add the integer 42 to the i-ith position in the list.
    def insert(self, pos, val):
        new_liList = LinkedList(self.head, self.rest)
        for i in new_liList: #Conceptually, I hope I am in the ballpark at least. #CASEY: You're super close; I should have been more clear, but we want to use recursion here.
            if pos == 0:
                self.head = val
            else:
                for item in self.rest:
                    if pos == 1:
                        self.head = val
                    else if pos == sel.rest.size(): #CASEY: In python, "else if" blocks are denoted as `elif` blocks.
                        self.rest = val
                    else:
                        if item[:pos]:
                            item.prepend(val)


print("For the 6 methods described above, which are accessors and which are mutators?")

accessors = []
mutators = []

accessors.append("contains", "get")
mutators.append("append", "delete", "prepend", "insert")

print(accessors)
print(mutators)

print("Determine the computational complexity (in "Big O" notation) of the using the following methods on the LinkedList object you implemented:")

comp = "Computational Complexity: "

list_1 = LinkedList("D")
list_2 = LinkedList("C", list_1)
list_3 = LinkedList("B", list_2)
test_list = LinkedList("A", list_3)

	#Search to see if a value A is contained in the Linked List. (Note: it might not!)
print(test_list)
testArray.self.contains("A", self)
print(comp + "O(N^3): iterates through (multiple) for lists to find a value")

	#Delete the i-th entry from the Linked List, where where 0 < i < n.
testArray.self.delete(0, self)
print(testArray)
print(comp + "O(N): 1 for first (0th) index, or (i + 1) when i is the index passed as a parameter of the .delete method")

	#Retrieve the i-th entry from the LinkedList, where 0 < i < n.
testArray.get(0, self)
print(comp + "O(N^2)")

	#Prepend (insert at the beginning) a new value B into the Linked List.
testArray.prepend("AA", self)
print(testArray)
print(comp + "(O)1")

	#Append (insert at the end) a new value B into the Linked List.
testArray.append("Z", self)
print(comp + "(O)N: must continue until it finds a value that can't be pointed to (because it doesn't exist)")

	#Insert a new value B into the Linked List at position i, where 0 < i < n.
testArray.insert("E", self, 5, self)
print(comp + "O(N^2): iterates through (multiple) for lists to find a position, then adds a value")

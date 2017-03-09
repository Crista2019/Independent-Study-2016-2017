class LinkedList(object):
    def __init__(self, head, rest=None):
        self.head = head
        self.rest = rest

    def __repr__(self):
        return "{} --> {}".format(self.head, self.rest)

    # Complexity: O(n) where n is the number of elements in the LL.
    def size(self):
        if self.rest:
            return 1 + self.rest.size()
        else:
            return 1

    # Complexity: O(n) where n is the number of elements in the LL.
    def append(self, val):
        if self.rest == None:
            self.rest = LinkedList(val) # If there is no remaining LinkedList left, we can just add another with the new value we're trying to add.
        else:
            self.rest.append(val) # We'll recursively "defer" the append to the rest of the list.

    # Complexity: O(n) where n is the number of elements in the LL.
    def contains(self, val):
        if self.head == val: # If this part of the LL contains the value, then we've found it! Easy peasy.
            return True
        elif self.rest: # If it didn't contain that LL, we should check if the `rest` of the LL has it.
            return self.rest.contains(val)
        else:
            return False # If there is no remaining LL and we didn't find the value, then it doesn't exist. That should cover all of the possible cases.

    # This one is complex. Go through some examples by hand to make sure you see what it's doing.
    # Complexity: O(n) where n is the number of elements in the LL. Technically we could say O(i) but we always want to think about the "worst" case. Here, that is i=n.
    def delete(self, i):
        if self.rest: # If there is nothing left, then we can't actually delete anything after this point.
             if i==0:
                 self.head = self.rest.head
                 self.rest = self.rest.rest # Keep in mind that `self.rest` is a LL -- therefore it has a `rest` property that we can use to see what follows it.
             else:
                 self.rest.delete(i-1) # We'll recurse on `i` -- that means we'll keep decrementing `i` until we reach out "base case" where i==0. At that point, we've reached the point we want to delete.

    # Complexity: O(n) where n is the number of elements in the LL. Technically we could say O(i) but we always want to think about the "worst" case. Here, that is i=n.
    def get(self, pos):
        if pos == 0:
            return self.head
        elif self.rest:
            return self.rest.get(pos-1)
        else:
            raise Exception("Oh no! I don't have that many elements!")

    # Complexity: O(1) or O(c), or in other words this is "constant time". This means that no matter how "big" the LL is, it will always perform the same amount of "work" to prepend a value.
    def prepend(self, val):
        new_liList = LinkedList(self.head, self.rest)
        self.head = val
        self.rest = new_liList

    # Complexity: O(n) where n is the number of elements in the LL. Technically we could say O(i) but we always want to think about the "worst" case. Here, that is i=n.
    def insert(self, pos, val):
        if pos==0:
            new_liList = LinkedList(self.head, self.rest) #Note that this code is effectively the same as prepend! We could even call it here...
            self.head = val
            self.rest = new_liList
        elif self.rest:
            self.rest.insert(pos-1, val)
        else:
            raise Exception("Oh no! I don't have that many elements!")

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
print "All tests pass! Woohoo!"

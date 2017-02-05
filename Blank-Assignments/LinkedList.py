class LinkedList(object):
  # Our LinkedList will be constructed by combining a bunch of other LinkedLists.
  # In this way, we can actually think of the LinkedList literally as a bunch of lists
  # that are linked together. 
  def __init__(self, head, rest=None):
    self.head = head
    self.rest = rest

  # This "__repr__" function tells Python how to "print" our custom LinkedList object.
  # Without it, Python would just print the memory reference of the object. You can
  # see that if you delete this function and call the test suite below.
  # 
  # Note that the "last" or tail-most LinkedList isn't special really. It just doesn't
  # doesn't point to another LinkedList. Each LinkedList really only "knows" about its
  # immediate successor; that's why this is implementation is also known as a 
  # singly-LinkedList. A doubly-LinkedList would have *two* references to other LinkedLists.
  def __repr__(self):
    return "{} --> {}".format(self.head, self.rest)

  # This is a prime example of recursion, which is a way of writing a program, which is
  # "when a thing is defined in terms of itself or of its type". In this case, the "size"
  # of the LinkedList we're checking is defined in terms of the "size" of its referenced
  # LinkedList. Realistically, the LinkedList doesn't know how big it is; it just knows that
  # it is one unit larger than the LinkedList that it's pointing to.
  def size(self):
    if self.rest:
      return 1 + self.rest.size()
    else:
      return 1

  # This method will insert a new_value at the front of the LinkedList. The tricky part
  # here is that we don't want to "forget" about the old "head" of the LinkedList. To
  # get around that, we'll copy the current head into a new LinkedList and mutate the 
  # current head into a head that contains the new_value.
  # 
  # Example:
  # LL(2).prepend(1) --> LL(1, LL(2))
  # LL(2, LL(3)).prepend(1) --> LL(1, LL(2, LL(3)))
  def prepend(self, new_value):
    new_linked_list = LinkedList(self.head, self.rest)
    self.head = new_value
    self.rest = new_linked_list

    # We're not going to return anything here. We've already changed the "self" object, so
    # there is no reason to return anything. Traditional "mutator" functions like this often
    # don't return anything, actually. They just modify the object and leave it at that.

  # You'll want to use recursion here too. Think of it this way: if a LinkedList is pointing
  # to a LinkedList already, then it really can't store the new_value -- but perhaps the 
  # next LinkedList can! So we might tell the "rest" of the LinkedList that we need to append
  # the new_value. At some point, we'll reach a LinkedList that doesn't point to another
  # LinkedList; at that point, we can create a new LinkedList object and tell that terminal
  # LinkedList that this new object will be the *new* end of the LinkedList.
  #
  # Examples:
  # LL(1).append(2) --> LL(1, LL(2)) 
  # LL(1, LL(2, LL(3))).append(4) --> LL(1, LL(2, LL(3, LL(4)))) 
  def append(self, new_value):
    pass

  # This is basically the same as "append", but with a new caveat: we want to *choose*
  # the position that the new_value will take in the LinkedList. When we "recurse", we'll
  # want to decrement desired_position until we hit the desired point, at which we can inject
  # a new LinkedList and reconfigure the pointers on the "self" and "self.rest" LinkedLists.
  #
  # Examples:
  # LL(1).insert(2,1) --> LL(1, LL(2)) # In this example, we also could have just used "append". :-)
  # LL(1, LL(3)).insert(2, 1) --> LL(1, LL(2, LL(3)))
  def insert(self, new_value, desired_position):
    pass

  # Think of this similarly to "insert" in a recursive mindset. Really, the tricky part here
  # is reconfiguring the pointers. How can we "forget" about a LinkedList without also 
  # forgetting about the "rest" of the LinkedList after the point we want to delete?
  #
  # Examples:
  # LL(1, LL(2)).delete(0) --> LL(2)
  # LL(1, LL(2, LL(3))).delete(1) --> LL(1, LL(3))
  def delete(self, position_to_delete):
    pass


# Now let's combine a bunch of LinkedLists together to create a list of animals.
list_a = LinkedList("cat")
list_b = LinkedList("dog", list_a)
list_c = LinkedList("bird", list_b)
animal_list = LinkedList("turtle", list_c)

# Effectively, we have one LinkedList that contains all of the animals, but you 
# can see above that we really are creating a bunch of lists that all "point"
# to eachother. We can see that below if we print the main "animal_list".
print "Our List: ", animal_list
print "Size: ", animal_list.size()

print "\n"

# Oh! But we forget our favorite animal -- the purple-spotted platypus! Let's add it.
animal_list.prepend("purple-spotted platypus")
print "Our Updated List: ", animal_list
print "Size: ", animal_list.size()

print "\n"

# We don't need to use all the variables though! We could just pass everything in as arguments.
print "Another List: ", LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))


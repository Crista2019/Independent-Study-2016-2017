"""
You've been contracted to develop a phonebook! Implement the methods below
using a dictionary as the internal representation of the data.
When you finish, the tests below should pass.
Define the complexity of each method as well. Note how the complexity would be
different if you used an array to store the phone numbers.
"""

class PhoneBook(object):
  def __init__(self): #COMPL total: O(1)
    self.phonebook = {} #COMPL: O(1)
 
# Add/update a person's number in the phonebook.
  def set_number(self, person, phone_number): #COMPL total: O()
    self.phonebook[person] = phone_number #COMPL: O(1)
 
# Return a person's phone number. If it isn't found, return "Not found!"
  def get_number(self, person): #COMPL total: O(1)
    if person in self.phonebook.keys(): 
      return self.phonebook[person] #COMPL: O(1)
    else:
      return "Not found!" #COMPL: O(1)

# Return the size of the phone book.
  def size(self): #COMPL total: O(1)
    return len(self.phonebook) #COMPL: O(1)
 
# Print the phonebook's contents in alphabetical order.
# Put one name and number on each line, separated by a colon.
  def pretty_print(self): #COMPL total: O(n)
    for x in sorted(self.phonebook.keys()): #COMPL: O(n)
      print(x + ": " + self.phonebook[x]) #COMPL: O(1)


def test_phonebook():
  book = PhoneBook()
  assert(book.size() == 0)
  book.set_number("Chuck Norris", "123-456-7890")
  book.set_number("Jackie Chan", "456-123-4560")
  book.set_number("Bruce Lee", "789-123-1230")
  assert(book.size() == 3)
  book.set_number("Bruce Lee", "789-123-1231")
  assert(book.get_number("Bruce Lee") == "789-123-1231")
  assert(book.size() == 3)
  book.pretty_print()

test_phonebook()

"""
Let's think about the universe. There are a lot of stars and 
lots of mass, but most of the universe is just empty space.
What if we needed a computer program that simulated the universe
and reported if an object was at a particular position?
We could keep track of every single point, but that's wasteful. Almost
every point would be empty. Hmm, so how could we store all this data?
Enter: the Sparse Array! A sparse array is like an array with a default
value. For example, we could keep track of all of the things in space!
Now if we have billions of spots to keep track of in our SparseArray, we 
really only need to worry about the spots that are "different" (ie: not empty).
Implement the methods below and determine the complexity of your implementation.
How would the performance of the SparseArray change if we increased the "size" of the area
of space we were looking at? How does it scale with the number of objects we store?
Reading: https://en.wikipedia.org/wiki/Sparse_array
"""
class SparseArray(object):
  def __init__(self, default): #COMPL total: O(1)
    self.data = {} #COMPL: O(1)
    self.default = default #COMPL: O(1)

# Record that `value` is at position (x,y,z).
  def insert(self, x, y, z, value): #COMPL total: O(1)
    self.data[(x,y,z)] = value #COMPL: O(1)

# Return the value found at position (x,y,z), or the default value if nothing is there.
  def query(self, x, y, z): #COMPL total: O(1)
    if (x,y,z) in self.data.keys(): 
      return self.data[(x,y,z)] #COMPL: O(1)
    else:
      return self.default #COMPL: O(1)

# Return the number of elements contained in this SparseArray.
  def size(self): #COMPL total: O(1)
    return len(self.data.items()) #COMPL: O(1)


from random import random
def test_sparse_array():
  space = SparseArray("Empty Space")
  space.insert(50.0, 39999.0, 23123.0, "Earth!")
  space.insert(13423.1, 123123.55, 395893.3, "Mars!")
  space.insert(83.593, 845839.3, 2938423.2, "Jupiter!")
  assert (space.query(83.593, 845839.3, 2938423.2) == "Jupiter!")

  assert (space.query(1,2,3) == "Empty Space")

  for planet_id in range(1000):
    space.insert(random(), random(), random(), "Planet {}".format(planet_id))

  assert (space.size() == 1003)

test_sparse_array()

"""
CASEY:
Overall feedback: Make sure you run each file before "submitting" it via git. Some of them have compilation issues; if you know one of them is broken, be sure to 
call that out since it helps me know which things didn't make sense. :-)
"""

"""
Stacks are a useful data structure that can be thought of in many ways as a "limited" list.
The basic idea of the Stack data structure is that it stores things in a "Last-In, First-Out"
manner; in other words, the item most recently put in the stack will be the item that comes out
of the stack soonest.
For example, think of a deck of cards. If we put more cards on top of the deck, we'll need to
take those cards off again before we can access the cards underneath. A stack data structure
makes this easy by providing an interface that can "push" things onto the stack and "pop" them
off again. Many stack implementations also allow us to "peek" at the top-most element on the stack.
An important component of a stack data structure is that we really never need to worry about the
items below the top of the stack.
Tasks:
1.) Read through this for more: https://www.tutorialspoint.com/data_structures_algorithms/stack_algorithm.htm [DONE]
2.) Implement the remaining methods on the Stack implementation below. [DONE]
3.) Run the provided tests below to check your code. Feel free to add more tests. [DONE]
4.) Describe the computational complexity of each of the stack methods below.
"""
class Stack(object):

  def __init__(self):
    self.data = []

  def __repr__(self):
    return "{}".format(self.data)

  def size(self, index=0, stackSize=0):
    #BASE CASE
    if index == len(self):
      return stackSize
      #RECURSIVE CASE
    else:
      size(self, index+1, stackSize+1)
    
    
    #return len(self.data) #This should return the number of elements in a stack

  def is_empty(self):
    return bool(self.data == []) #return either True or False for an instance of a blank array

  def push(self, new_val, index=0):
    #BASE CASE
    if index == len(self.data)-1:
      #new value (i.e. 'top') will be defined as the last index of the data list (i.e. self.data.size() - 1)
      self.data.append(new_val)
      return self
    #RECURSIVE CASE
    else:
      push(self, new_val, index+1)

  def pop(self, index=0):
    if index == len(self.data)-1:
      del self.data[index]
      return self
    #RECURSIVE CASE
    else:
      pop(self, index+1)

  def peek(self, index=0):
    if index == len(self.data)-1: #Again, top is the last data element, but it is easier to visualize LIFO that way. The last in is the last index value.
      return self.data[index]
    #RECURSIVE CASE
    else:
      peek(self, index+1)
    
test_stack = Stack()
test_stack.is_empty()
test_stack.push(1)
test_stack.pop()
test_stack.is_empty()
test_stack.push('A')
test_stack.push('B')
test_stack.push('C')
test_stack.peek()
   
def run_tests():
  print("\nRunning tests!... \n")
  s = Stack()
  test_vals = [1,2,3]

  print("Stack should be empty -- {}").format("CORRECT" if s.is_empty() else "INCORRECT")
"""
  for new_top in test_vals:
    s.push(new_top)
    print("New top should be {} -- {}").format(new_top, "CORRECT" if new_top==s.peek() else "INCORRECT")

  print("Size should be size {} -- {}").format(len(test_vals), "CORRECT" if len(test_vals)==s.size() else "INCORRECT")

  print("Stack should not be empty -- {}").format("CORRECT" if not s.is_empty() else "INCORRECT")

  for i, val in enumerate(test_vals[::-1]):
    print("Popped value should be {} -- {}").format(val, "CORRECT" if val==s.pop() else "INCORRECT")
    print("Size should be size {} -- {}").format(len(test_vals)-(i+1), "CORRECT" if len(test_vals)-(i+1)==s.size() else "INCORRECT")

  print("Stack should be empty again -- {}").format("CORRECT" if s.is_empty() else "INCORRECT")

run_tests()"""

"""
COMPUTATIONAL COMPLEXITY OF STACK OBJECT'S METHODS:
.size()
  O(1). Rather than iterating through every value, getting the length of a data set returns the already known sum of its elements.
.isEmpty()
  O(1). This method just checks to see if the stack is an empty list. That is the most work it will do because computers are lazy that way.
.push()
  O(1). Regardless of stack size (# of data elements), the implementation will always perform this method in the same amount of time.
        The new element is just getting pushed to the top
.pop()
  O(k). k = size of new slice. Because the data is getting shifted as a result ok this implementation of pop(), it considers it as .pop(n) where n = the specified index instead of .pop(), which assumes the last index as the value getting removed.
 
.peek()
  O(1). Regardless of stack size (# of data elements), the implementation will always perform this method in the same amount of time.
        ^Same as .pop(). Indexing = get() is only accessing 1 specific value 1 time.
"""

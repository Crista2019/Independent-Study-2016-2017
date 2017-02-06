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
1.) Read through this for more: https://www.tutorialspoint.com/data_structures_algorithms/stack_algorithm.htm
2.) Implement the remaining methods on the Stack implementation below. 
3.) Run the provided tests below to check your code. Feel free to add more tests.
4.) Describe the computational complexity of each of the stack methods below.

"""
class Stack(object):
  # Our constructor will only create an "empty" stack by design.
  # If we want to add things to it, we'll need to use the methods
  # that we're going to define below. Don't worry about changing
  # anything here.
  def __init__(self):
    self.data = []
 
  def __repr__(self):
    return "{}".format(self.data)

  # Return the number of things in the stack. This is an accessor, so return the value.
  def size(self):
    pass

  # Return True if the stack is empty and False otherwise. 
  # This function is an accessor.
  def is_empty(self):
    pass
  
  # Push a new value on top of the stack. 
  # Don't return anything; this is a mutator.
  #
  # Example
  # some_stack = Stack()
  # some_stack.push(1)
  # # We don't return anything, but some_stack now has "1" on top.
  def push(self, new_val):
    pass

  # Return the top thing on our stack *and* remove it from the stack.
  # This function is both a mutator *and* and accessor.
  # 
  # Example:
  # some_stack.push(2)
  # some_stack.push(1)
  # some_stack.pop() --> 1
  # some_stack.pop() --> 2
  def pop(self):
    pass

  # Return the top thing on our stack, but leave the stack unchanged.
  # This is an accessor, so return the value.
  # 
  # Example:
  # some_stack.push(1)
  # some_stack.peek() --> 1
  # some_stack.peek() --> 1 # Unlike "pop", "top" doesn't change the stack.
  def peek(self):
    pass

def run_tests():
  print "\nRunning tests!... \n"
  s = Stack()
  test_vals = [1,2,3]

  print "Stack should be empty -- {}".format("CORRECT" if s.is_empty() else "INCORRECT")

  for new_top in test_vals:
    s.push(new_top)
    print "New top should be {} -- {}".format(new_top, "CORRECT" if new_top==s.peek() else "INCORRECT")

  print "Size should be size {} -- {}".format(len(test_vals), "CORRECT" if len(test_vals)==s.size() else "INCORRECT")

  print "Stack should not be empty -- {}".format("CORRECT" if not s.is_empty() else "INCORRECT")

  for i, val in enumerate(test_vals[::-1]):
    print "Popped value should be {} -- {}".format(val, "CORRECT" if val==s.pop() else "INCORRECT")
    print "Size should be size {} -- {}".format(len(test_vals)-(i+1), "CORRECT" if len(test_vals)-(i+1)==s.size() else "INCORRECT")

  print "Stack should be empty again -- {}".format("CORRECT" if s.is_empty() else "INCORRECT")

run_tests()




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

  def size(self):
    return len(self.data) #This should return the number of elements in a stack

  def is_empty(self):
    return self.data == [] #return either True or False for an instance of a blank array

    """if self.data.size() < 1: This states that if there is 1 or more (i.e. any) elements in the stack, the stack is not empty, and it returns False
      return True               I decided that this was mostly unnecessary code.
    else:
      return False"""
  
  def push(self, new_val):
    self.data.append(new_val) #new value (i.e. 'top') will be defined as the last index of the data list (i.e. self.data.size() - 1)

  def pop(self):
    return self.data[self.data.size() - 1] #returns top (last element is considered top)
    return self.data.pop() #Is this legal?

  def peek(self):
    return self.data[self.data.size() - 1] #Again, top is the last data element, but it is easier to visualize LIFO that way. The last in is the last index value.

#I had to make the test function Python 3 compatable. (Just in the print functions and such. :)
def run_tests():
  print("\nRunning tests!... \n")
  s = Stack()
  test_vals = [1,2,3]

  print("Stack should be empty -- {}").format("CORRECT" if s.is_empty() else "INCORRECT")

  for new_top in test_vals:
    s.push(new_top)
    print("New top should be {} -- {}").format(new_top, "CORRECT" if new_top==s.peek() else "INCORRECT")

  print("Size should be size {} -- {}").format(len(test_vals), "CORRECT" if len(test_vals)==s.size() else "INCORRECT")

  print("Stack should not be empty -- {}").format("CORRECT" if not s.is_empty() else "INCORRECT")

  for i, val in enumerate(test_vals[::-1]):
    print("Popped value should be {} -- {}").format(val, "CORRECT" if val==s.pop() else "INCORRECT")
    print("Size should be size {} -- {}").format(len(test_vals)-(i+1), "CORRECT" if len(test_vals)-(i+1)==s.size() else "INCORRECT")

  print("Stack should be empty again -- {}").format("CORRECT" if s.is_empty() else "INCORRECT")

run_tests()

"""
COMPUTATIONAL COMPLEXITY OF STACK OBJECT'S METHODS:

.size()
  O(n). This method instrinsically depends on the quantity of elements in the stack of data. As a result, the return values varies.

.isEmpty()
  O(1). This method just checks to see if the stack is a black list. That is the most work it will do because computers are lazy that way.

.push()
  O(1). Regardless of stack size (# of data elements), the implementation will always perform this method in the same amount of time. 
        The new element is just getting added (appended) to the top

.pop()
  O(1). Regardless of stack size (# of data elements), the implementation will always perform this method in the same amount of time. 
        ^Same as .push();

.peek()
  O(1). Regardless of stack size (# of data elements), the implementation will always perform this method in the same amount of time. 
        ^Same as .pop(); However, it is only 'accessing' and not 'mutating' the top value 

"""
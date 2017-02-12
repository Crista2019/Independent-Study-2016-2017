
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

  def size(self):
    return len(self.data) #This should return the number of elements in a stack

  def is_empty(self):
    return self.data == [] #return either True or False for an instance of a blank array

    # CASEY: Yup, it was unnecessary; I just wanted to make sure you had the right idea for what was going on here. :-)
    """if self.data.size() < 1: This states that if there is 1 or more (i.e. any) elements in the stack, the stack is not empty, and it returns False
      return True               I decided that this was mostly unnecessary code.
    else:
      return False"""

  def push(self, new_val):
    self.data.append(new_val) #new value (i.e. 'top') will be defined as the last index of the data list (i.e. self.data.size() - 1)

  def pop(self):
    return self.data[self.data.size() - 1] #returns top (last element is considered top) #CASEY: Neeeearly there. Recall that "pop" also mutates the list by removing the "top" from the stack.
    return self.data.pop() #Is this legal? #CASEY: Haha, technically -- but that's just because Python's lists have lots of nifty features. The line above was what I was leaning towards. :-)

    # CASEY: A way you might do this is as follows (though the "pop" list method that Python gives you is a shortcut as you mentioned above.)
    top = self.data.peek()
    self.data = self.data[:-1]
    return top

  def peek(self):
    return self.data[self.data.size() - 1] #Again, top is the last data element, but it is easier to visualize LIFO that way. The last in is the last index value.
    # CASEY: One minor thing: "self.data" is a python list so it doesn't have a "`size` method; to get the size of one of those you'd use `len(self.data)`.

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
  #CASEY: If the internal data in our Stack was stored as a LinkedList, then you're right that we'd need to check to see how many values
          were contained in a one-by-one method. However, since we're using the Python list's "len" method, we should see the computational
          complexity of *that* method: https://wiki.python.org/moin/TimeComplexity . It turns out, it can do it in O(1) -- aka, "constant" time!
          It does that by keeping a "counter" of how many values it already contains; that way, it doesn't need to count everything every time
          we ask because it already has the answer.

.isEmpty()
  O(1). This method just checks to see if the stack is a black list. That is the most work it will do because computers are lazy that way.
  #CASEY: Yup! If by "black" list here you mean an "empty" list. I've never seen it referred to as a "black" list before. :-)

.push()
  O(1). Regardless of stack size (# of data elements), the implementation will always perform this method in the same amount of time.
        The new element is just getting added (appended) to the top
  #CASEY: Yup! And since we're using Python's "append" method inside of our Stack's "push" method, let's refer to that
          documentation: https://wiki.python.org/moin/TimeComplexity .

.pop()
  O(1). Regardless of stack size (# of data elements), the implementation will always perform this method in the same amount of time.
        ^Same as .push();
  #CASEY: Yup! Be careful though, as there are *some* caveats to Python's list's "pop" method:
          http://stackoverflow.com/questions/195625/what-is-the-time-complexity-of-popping-elements-from-list-in-python
          If you implement it without the "pop" as I wrote above, you'd actually be creating a new "slice", which is O(k) where k is
          the size of the new slice.

.peek()
  O(1). Regardless of stack size (# of data elements), the implementation will always perform this method in the same amount of time.
        ^Same as .pop(); However, it is only 'accessing' and not 'mutating' the top value
  #CASEY: Yup! Note that indexing a list (ie, which is the same as using the "get" method of the list) is O(1), so we're verified:
          https://wiki.python.org/moin/TimeComplexity#list .

"""

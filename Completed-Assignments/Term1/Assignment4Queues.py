"""
QUEUES
A queue is an ordered collection of items where the addition of new items happens at one end, called the “rear,” 
and the removal of existing items occurs at the other end, commonly called the “front.” 
As an element enters the queue it starts at the rear and makes its way toward the front, 
waiting until that time when it is the next element to be removed.

The most recently added item in the queue must wait at the end of the collection. 
The item that has been in the collection the longest is at the front. 
This ordering principle is sometimes called FIFO, first-in first-out. It is also known as “first-come first-served.”

The simplest example of a queue is the typical line that we all participate in from time to time. 
We wait in a line for a movie, we wait in the check-out line at a grocery store, and we wait in the cafeteria line (so that we can pop the tray stack). 
Well-behaved lines, or queues, are very restrictive in that they have only one way in and only one way out. 
There is no jumping in the middle and no leaving before you have waited the necessary amount of time to get to the front. 
Figure 1 shows a simple queue of Python data objects.


Tasks:
1.) Read through this for more: https://interactivepython.org/runestone/static/pythonds/BasicDS/WhatIsaQueue.html
2.) Implement the remaining methods on the Queue implementation below. 
3.) Run the provided tests below to check your code. Feel free to add more tests. 
4.) Describe the computational complexity of each of the Queue methods below.
"""
class Queue(object):

  def __init__(self):
    self.data = []

  def __repr__(self):
    return "{}".format(self.data)

  def size(self):
    return len(self.data)
    
  def isEmpty(self):
    return bool(self.data == [])

  def enqueue(self, item):
    self.data.insert(0, item)

  def dequeue(self):
    return self.data.pop()

    
test_Queue = Queue()
test_Queue.isEmpty()
test_Queue.enqueue("Apples")
test_Queue.enqueue("Bananas")
test_Queue.size()
test_Queue.dequeue()
test_Queue.size()
test_Queue.enqueue("Cranberries")
test_Queue.size()

"""   
def run_tests():
  print("\nRunning tests!... \n")
  q = Queue()
  test_vals = [1,2,3]

  print("Queue should be empty -- {}").format("CORRECT" if q.isEmpty() == True else "INCORRECT")
  
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)

  for val in test_vals:
    q.enqueue(val)
    print("New rear should be {} -- {}").format(val, "CORRECT" if q[0] == val else "INCORRECT")
  print("Size should be size {} -- {}").format(len(test_vals), "CORRECT" if len(test_vals)==q.size() else "INCORRECT")
  print("Queue should not be empty -- {}").format("CORRECT" if not q.isEmpty() else "INCORRECT")
  for i, val in enumerate(test_vals[::-1]):
    print("Dequeued value should be {} -- {}").format(val, "CORRECT" if val==q.dequeue() else "INCORRECT")
    print("Size should be size {} -- {}").format(len(test_vals)-(i+1), "CORRECT" if len(test_vals)-(i+1)==q.size() else "INCORRECT")
  print("Queue should be empty again -- {}").format("CORRECT" if q.isEmpty() else "INCORRECT")

run_tests()
"""

"""
COMPUTATIONAL COMPLEXITY OF QUEUE OBJECT'S METHODS:
.size() = O(1) Finding the length of all data in the queue.
 
.isEmpty() = O(1) Returning a boolean value of True or False depending on whether the queue object is currently a value-less list

.enqueue() = O(n) For this implementation, positio 0 in the queued list is considered the "rear". Therefore, insert() can be used to add a new value to the rear.

.dequeue() = O(1) ... This also means that pop() can be used to remove the "front element of a queue, which would be the last index of the list
 
"""

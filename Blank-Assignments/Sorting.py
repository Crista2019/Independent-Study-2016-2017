
"""
Alrighty! Now that we've studied a few different data structures and realized there are lots of
different ways to represent our data, it's time to realize that there are also lots of ways
to act upon each those representations! In this assignment, we'll sort Python lists in different ways.

Why are there so many ways to sort lists? Well, each algorithm has trade-offs. Some require more memory;
some are much slower; some are slightly more complex to think about. Many of these trade-offs will
become apparent as we implement the sorting functions below. 

Implement each function as a mutator.
That is, the functions should not return anything but instead should operate directly on the `array` 
parameter. For example:

x = [1,4,5,2,4] 
bubble_sort(x)
assert( x == [1,2,4,4,5])

Reading:
-- http://www.studytonight.com/data-structures/introduction-to-sorting
-- https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms
-- http://www.cs.cmu.edu/~clo/www/CMU/DataStructures/Lessons/lesson8_1.htm

This animation helps differentiate what each algorithm does: https://www.toptal.com/developers/sorting-algorithms

TASK: Implement the following sorting algorithms based on your reading.
TASK: Analyze the computational complexity of each function. 
TASK: Think briefly about when you might prefer each sorting algorithm over the others.
"""

def bubble_sort(array):
  pass

def insertion_sort(array):
  pass
  
def selection_sort(array):
  pass

def quick_sort(array):
  pass

def merge_sort(array):
  pass

def run_sorting_tests():
  import random, time
  num_elements = 1000
  print "Running tests using {} elements...".format(num_elements)  
  for sorter in [bubble_sort, insertion_sort, selection_sort, quick_sort, merge_sort]:
    try:
      t_start = time.time()
      array = range(num_elements)
      random.shuffle(array)
      sorter(array)
      t_end = time.time()
      assert array == sorted(array)
      print "Woohoo! `{}` completed in {} seconds.".format(sorter.__name__, t_end-t_start)
    except Exception as e:
      print "Uh oh! The sorting function `{}` isn't correct.".format(sorter.__name__)
      raise e

run_sorting_tests()

"""
Up next... read about min-heaps and max-heaps!
"""

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

#Bubble - rearrange pairs of elements which are out of order, until no such pairs remain.
def bubble_sort(array): #Computational Complexity: O(n^2)
  for val in range(len(array)-1,0,-1):
    for i in range (val):
      if array[i] > array[i+1]:
        placeholder = array[i]
        array[i] = array[i+1]
        array[i+1] = placeholder

#Insertion - putting an element in the appropriate place in a sorted list yields a larger sorted list.
def insertion_sort(array): #Computational Complexity: O(n^2)
  for i in range(1, len(array)):
    currentIndex = array[i]
    place = i

    while place > 0 and array[place-1] > currentIndex:
      array[place] = a[place-1]
      place -= 1

    array[place] = currentIndex      
  
#Selection - extract the largest element form the list, exchange with the last element in the current list, and repeat.
def selection_sort(array): #Computational Complexity: O(n^2)
  for val in range(len(array)-1,0,-1):
    maxIndex=0
    for place in range(1,val+1):
      if array[place] > array[maxIndex]:
        maxIndex = place
    placeholder = array[val]
    array[val] = array[maxIndex]
    array[maxIndex] = placeholder

#Quick - divide and conquer algorithm which based on a partition operation, elements < partition element and > partition element are sorted seperately
def quick_sort(array, start, end): #Computational Complexity: O(n log n)
  if start < end:
    pivot = partition(array, start, end)
    quick_sort(array, start, pivot-1)
    quick_sort(array,pivot+1 end)

def partition(array, start, end):
  pivot = array[start]
  left = start + 1
  right = end
  done = False
  while not done:
    while left <= right and array[left] <= pivot:
      left += 1
    while array[right] >= pivot and right >= left:
      right -= 1
    if right < left:
      done = True
    else: 
      #Swapping left and right
      placeholder = array[left]
      array[left] = array[right]
      array[right] = placeholder
    placeholder = array[start]
    array[start] = array[right]
    array[right] = placeholder

#Merging - Two sorted lists can be easily combined to form a sorted list.
def merge_sort(array): #Computational Complexity: O(n log n)
  #Dividing array
  if len(array) > 1:
    partition = len(array)//2
    left = array[:partition]
    right = array[partition:]

    merge_sort(left) #Recuuuursssion
    merge_sort(right)

    i,j,k= 0,0,0

    while i < len(left) and j  len(right):
      if left[i]  right[i]:
        array[k] = left[i]
        i += 1
      else:
        array[k] = right[j]
        j += 1
      k += 1

    while i < len(left):
      array[k] = left[j]
      i += 1
      k += 1

    while j < len(right):
      array[k] = right[j]
      j += 1
      k == 1

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


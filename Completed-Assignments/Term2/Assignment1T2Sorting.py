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
    #print(val)
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
      array[place] = array[place-1]
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
def quick_sort_helper(array): #Computational Complexity: O(n log n)
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quick_sort_helper(less)+equal+quick_sort_helper(greater)
    else:
        return array
        
def quick_sort(array):
    sorted_array = quick_sort_helper(array)
    
    #Now that we have the sorted array, let's assign each value in our array:
    for i in range(len(array)):
        array[i] = sorted_array[i]
        
"""        
CASEY: Your implementation of quick_sort is good! Though it "returns" the new array
rather than changing the original array itself. You can get around this by turning
your function above into a "helper" function and then by having the "main" quick_sort
function just call that. I've made that change above. :-)
"""

"""
#Merging - Two sorted lists can be easily combined to form a sorted list.
def merge(left,right):
    newArray = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            newArray.append(left[0])
            left.remove(left[0])
        else:
            newArray.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        newArray += right
    else:
        newArray += left
    return newArray
    
def merge_sort(array):#Computational Complexity: O(n log n)
    if len(array) == 0 or len(array) == 1:
      pass
    else:
      middle = int(len(array)/2)
      left = merge_sort(array[0:middle])
      right = merge_sort(array[middle:len(array)])
      return merge(left,right)
"""

def merge_sort_helper(array):
    if len(array) < 2:
        return array
    else:
      # Cut the list in half and sort both halves....
      left_half = merge_sort_helper(array[:len(array)/2])
      right_half = merge_sort_helper(array[len(array)/2:])
      
      # Go through both halves and keep picking off the smaller value...
      sorted_array = []
      while(left_half and right_half):
          if left_half[0] < right_half[0]:
              sorted_array.append(left_half.pop(0))
          else:
              sorted_array.append(right_half.pop(0))
      
      # If there's any leftover, let's add it.
      if left_half:
          sorted_array += left_half
      elif right_half:
          sorted_array += right_half

      # Return the sorted array!
      return sorted_array
      

def merge_sort(array):
    sorted_array = merge_sort_helper(array)
    
    #Now that we have the sorted array, let's assign each value in our array:
    for i in range(len(array)):
        array[i] = sorted_array[i]    
    
            
print quick_sort([3,1,2,1,2,3])
def run_sorting_tests():
  import random, time
  num_elements = 3000
  print("Running tests using {} elements...").format(num_elements)  
  for sorter in [bubble_sort, insertion_sort, selection_sort, quick_sort, merge_sort]:
    try:
      t_start = time.time()
      array = range(num_elements)
      random.shuffle(array)
      sorter(array)
      t_end = time.time()
      assert array == sorted(array)
      print("Woohoo! `{}` completed in {} second").format(sorter.__name__, t_end-t_start)
    except Exception as e:
      print("Uh oh! The sorting function `{}` isn't correct.").format(sorter.__name__)
      raise e
run_sorting_tests()


"""
COMPARING "COMPARISON" SORTING ALGORITHMS:
Selection Sort: 
  ~unstable
  ~inplace
  ~running time: O(N^2)
  ~extra space: 1
Insertion Sort:
  ~stable 
  ~inplace
  ~running time: O(N) to O(N^2) #CASEY: Usually we just care about the "worst" case -- so we'll call this O(N^2)
  ~extra space: 1
  ~*depends on order of input keys
Quick Sort:
  ~unstable
  ~inplace
  ~running time: O(NlgN)
  ~*Probabilistic guarantees, depend on distribution of input key values
Merge Sort:
  ~stable
  ~not inplace
  ~running time: O(NlgN) 
Bubble Sort:
  ~stable
  ~space: O(1)
  ~time: O(N^2)
"""

"""
Up next... read about min-heaps and max-heaps!
"""

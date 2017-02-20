#Most Recent Work Day: 2/19/17
"""
TASK: Read these: 
 - https://www.cs.utah.edu/~germain/PPS/Topics/recursion.html (READ)
 - http://stackoverflow.com/questions/717725/understanding-recursion (READ)
 - http://www.programmerinterview.com/index.php/recursion/explanation-of-recursion/ (READ)
This also might be helpful:
 - http://softwareengineering.stackexchange.com/questions/25052/in-plain-english-what-is-recursion (READ)
"""

"""TASK: Go ahead and write a diagram to see what fib(4) returns.
fib(4)
  |    \
  |     \
  |      \
fib(3)  +   fib(2)  
  |      \            
  |       \        
  |        \        
fib(2)  +  fib(1)          
  |   \          \      
  |    \          \    
  |     \          \         
fib(1)  +  fib(0)    1         
  |         |
  |         |
  |         |
  1         0

TASK: Then, do one for fib(5). Feel free to just refer to our diagram above `fib(3)`
  to avoid making an absurdly large diagram

fib(5) 
  |  \
  |   \
  |    \
fib(4)  +  fib(3)  
  |      \      \     
  |       \      \       
  |        \      \     
fib(3) ...             
...
  """
def fib(n):
  if n<=0:
    return 0
  elif n==1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

def fib_loop(n):
  previous = 1
  current=0

  while (n>0):
    old_previous = previous
    previous = current # The old `current` value will now become the `previous` value.
    current = current + old_previous # Add the previous value to the current value to create a "new" current value.
    n -= 1 # Decrement the number of steps we have left.
  return current

# Let's just double-check that everything is hunky-dory with our loop function.
assert fib_loop(5) == fib(5)
assert fib(5) == 5 # The 5th Fib element is actually "5", conveniently enough.
print("Woohoo! All tests pass!")

"""TASK: Read this: https://www.quora.com/What-are-some-easy-ways-to-understand-and-calculate-the-time-complexity-of-algorithms (READ)

    def fib_loop(n): 
        previous = 1 #COMPL: O(1)
        current=0 #COMPL: O(1)
    
        while (n>0): #COMPL: EverythingContainedHere * n = O(1+1+1+1) * n = O(1) * n = O(n)
            old_previous = previous #COMPL: O(1)
            previous = current #COMPL: O(1)
            current = current + old_previous #COMPL O(1)
    
            n -= 1 #COMPL: O(1) 
    
        return current #COMPL: O(1)
The complexity of our loop function is the sum of all the complexities of the steps it contains. This comes
out to be a bunch of O(1)s with an O(n). Since for really large `n` the 1s don't contribute much, we actually
can just "absorb" them. So our complexity for the function comes out to be O(n). That's much quicker than our
previous function! That doesn't mean we should always use `fib_loop`; the `fib` function is cleaner and
easier to understand on a quick read-through.
Just to drive home what "complexity" really means, let's actually time these functions to see how they act differently.
Run this script and look at the output of the `time_it` calls below. Note that the recursive function takes *much*
longer to run; meanwhile, the loop version actually completes pretty quickly! Thanks to our complexity estimate, we
didn't actually need to run the functions to know that the loop version would be faster. Neato.
"""
# A helper function to help us time our `fib` functions.
def time_it(function, val):
    import time
    start_time = time.time()
    function(val)
    time_taken = time.time() - start_time
    print("Time taken for {}({}): {} seconds".format(function.__name__, val, time_taken))


print("Performing time tests!")
time_it(fib_loop, 30) # O(n)
time_it(fib, 30) # O(2^n)

"""
Now, let's write up some other recursive functions. Run this script in order to "test" your implementation. Everything should pass.
These are tricky, so be sure to work out examples by hand and *then* write up your algorithms. If you get stuck, take a step back
and do an example by hand. Try to break the "big" problem into a smaller-sized problem; that's the key to recursion.
"""
def test(actual, expected):
    if actual != expected: print("Uh oh! Expected '{}' but got '{}'".format(expected, actual))

# This function should return the sum of all numbers up to and including `n`.
# TASK: Fix this function using recursion. The tests below should pass. (DONE)
# TASK: Estimate the complexity for each line of your function as a comment on that line. Then use those to estimate the complexity of the function. (DONE)
def sum_up_to_n(n): #O(1) + O(1) + O(1) + O(n) = O(n)
  # TODO: Add Base Case
  the_sum = 0 #COMPL: O(1)
  if n == 0: #COMPL: O(1)
    return the_sum #COMPL: O(1)
  # TODO: Add Recursive Case
  return n + sum_up_to_n(n - 1) #COMPL: O(n) * >

test(sum_up_to_n(0), 0)
test(sum_up_to_n(1), 1)
test(sum_up_to_n(2), 3)
test(sum_up_to_n(3), 6)
test(sum_up_to_n(4), 10)

# This funciton will "flip" a list using recursion. It might be tempting to cheat with a loop or by using the_list[::-1], but refrain. ;-)
# TASK: Fix this function using recursion. The tests below should pass. (DONE)
# TASK: Estimate the complexity for each line of your function as a comment on that line. Then use those to estimate the complexity of the function. (DONE)
def flip_a_list(the_list): #O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(1+1) * O(n) = O(n)
    # TODO: Add Base Cases -- there should be two, one when the list is empty and one when the list has a single item in it.
    test_list = the_list #COMPL: O(1)
    new_list = [] #COMPL: O(1)
    currentIndex = len(test_list) - 1 #COMPL: O(1)
    if test_list == []: #COMPL: O(1)
      return [] #COMPL: O(1)
    elif currentIndex == 0: #COMPL: O(1)
      new_list.append(test_list[0]) #COMPL: O(1)
      return new_list #COMPL: O(1)
    # TODO: Add Recursive Case
    else:
      new_list.append(test_list[currentIndex]) #COMPL: O(1)
      del test_list[currentIndex]
      print(test_list, new_list)
      flip_a_list(test_list) #COMPL: O(n) * ^^

test(flip_a_list([]), [])
test(flip_a_list([1]), [1])
test(flip_a_list([2,1,2]), [2,1,2])
test(flip_a_list([3,2,1]), [1,2,3])

# This function will take a `value_to_add` and a list of numbers. It should return the list where each element has had value_to_add added to it.
# TASK: Fix this function using recursion. The tests below should pass.
# TASK: Estimate the complexity for each line of your function as a comment on that line. Then use those to estimate the complexity of the function. (DONE)
def add_to_list(value_to_add, the_list): #O(1) + O(1) + O(1+1) * O(n) = O(n)
    currentElement = len(the_list) - 1 #COMPL: O(1)
    # Add Recursive Case
    while currentElement >= 0: #COMPL: O(n) * >>
      the_list[currentElement] += value_to_add #COMPL: O(1)
      currentElement -= 1 #COMPL: O(1)
    # TODO: Add Base Case
    else:
      return the_list #COMPL: O(1)




test(add_to_list(1, [0]), [1])
test(add_to_list(1, [1,2]), [2,3])
test(add_to_list(2, [1,2,3]), [3,4,5])

# This function will take a string and determine if it is recursive or not. If it is, it should return True; if not, return False.
# TASK: Fix this function using recursion. The tests below should pass. (DONE)
# TASK: Estimate the complexity for each line of your function as a comment on that line. Then use those to estimate the complexity of the function. (DONE)
def is_palindrome(string): #O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(1+1+1) * O(n) = O(n)
  firstVal = 0 #COMPL: O(1)
  lastVal = len(string) - 1 #COMPL: O(1)
  new_string = string #COMPL: O(1)
  # TODO: Add Base Case
  if string == "": #COMPL: O(1)
    return True #COMPL: O(1)
  # TODO: Add Recursive Case
  elif string[firstVal] == string[lastVal]: #COMPL: O(1)  
    new_string = new_string[1:] #COMPL: O(1)
    new_string = new_string[lastVal-1:] #COMPL: O(1)
    is_palindrome(new_string) #COMPL: O(n) * ^^^
  else:
     return False #COMPL: O(1)

test(is_palindrome(""), True)
test(is_palindrome("t"), True)
test(is_palindrome("cat"), False)
test(is_palindrome("tat"), True)
test(is_palindrome("tacocat"), True)
test(is_palindrome("taco cat"), False)

# This function will take a value `n` and return the factorial of n (mathematically "n!"). This is the same as n * (n-1) * (n-2) * ... * 1.
# TASK: Fix this function using recursion. The tests below should pass. (DONE)
# TASK: Estimate the complexity for each line of your function as a comment on that line. Then use those to estimate the complexity of the function. (DONE)
def factorial(n): # O(1) + O(1) + O(1+1) * O(n) = O(n)
  factorial = 1 #COMPL: O(1)
    # TODO: Add Recursive Case
  while n > 1: #COMPL: O(n) *>>
    factorial = factorial * n #COMPL: O(1)
    n = n - 1 #COMPL: O(1)
  # TODO: Add Base Case
  else:
    return factorial #COMPL: O(1)

test(factorial(0), 1)
test(factorial(1), 1)
test(factorial(2), 2)
test(factorial(3), 6)
test(factorial(4), 24)

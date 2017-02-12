
"""
Thinking recursively is a fundamental part of CS. It's essentially a way to 
write a function in terms of itself. 

This can help with proofs that functions
do what they're supposed to do, but also can help with OO design since it
can help us think about things in an isolated context. For example, in the
previous LinkedList lab, thinking recursively helps us think about each 
"component" of the LinkedList as an independent object as opposed to thinking
about the list as one giant blob.

At the core, recursion needs two things: (1) a "recursive" case where we 
continue performing recursive operations and (2) a "base" case where we
eventually *stop* recursion.

In this vein, we could think about recursion as a different way of writing
a `while` loop. In fact, all recursion can be replaced with `while` loops, 
but oftentimes at the cost of making code harder to understand.

Read this: https://www.cs.utah.edu/~germain/PPS/Topics/recursion.html
"""

"""
The Fibonacci sequence is a famous mathematic sequence where each number
in the sequence is the sum of the previous two. In other words, the sequence
is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
More on Fib: https://www.mathsisfun.com/numbers/fibonacci-sequence.html
"""

def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

"""
Now let's think about how this function actually runs. The obvious "weird"
part is that the function calls itself and continues to call litself in the
`else` block. This is the "recursive" point in our function; this is the point
where our function uses itself to solve the problem.

Another way to think about this is that our function, when given a "large"
problem, breaks down the problem into two "smaller" problems -- namely,
`fib(n-1)` and `fib(n-2)`. This idea -- "breaking down the problem into
smaller problems" -- is the core of recursive programming.

Now we just need to figure out when our function should "stop". Well, with
the Fibonacci sequence we have the first two numbers (0 and 1). Those are
NOT defined as the sum of the previous two numbers, so they make for two natural
"base" cases for our function above.

"""

"""
Let's take a look at the "Call Tree" of this function. A "Call Tree" is just
a diagram that shows us what returns; they're super helpful for dissecting
complex recursive programs. 

fib(3)
  |    \
  |      \
  |        \
fib(2)  +   fib(1)
  |   \          \
  |     \           \
  |       \            \
fib(1)  +  fib(0)       1
  |         |
  |         |
  |         |
  1         0

Thus, our diagram says fib(3) gets broken into `1 + 0 + 1`, which should return 2.

TASK: Go ahead and write a diagram to see what fib(4) returns.
TASK: Then, do one for fib(5). Feel free to just refer to our diagram above `fib(3)`
      to avoid making an absurdly large diagram. 

This Fibonacci implementation is an example of a O(2^n) function (aka, an "exponential complexity" function).
We can see this from our diagram for `fib(3)` above. Think about how much "work" our `fib(3)` needs to do. 
Well, `fib(3)` doubles its workload by performing two additional calls to itself with `fib(2)` and `fib(1)`.
Well, let's expand the problem a bit. What would `fib(4)` do? It would call `fib(3)` and `fib(2)` -- each of which
would double their own workload. More generally (for large values of "n"), `fib(n)` will always double its workload.
If we have to double something `n` times, that's 2*2*...*2 for however large `n` is; mathematically, that is just 2^n.
Thus, our complexity for this function is O(2^n).
For a (slightly complex, but more concrete) proof, see: 
http://stackoverflow.com/questions/360748/computational-complexity-of-fibonacci-sequence 
"""

"""
Now, I mentioned before that recursive functions can be written as `while` loops. Let's translate our `fib` function.
It won't be quite as pretty because we have to keep track of the state of things, but it's possible nonetheless.
"""

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
print "Woohoo! All tests pass!"

"""
So, our recursive Fibonacci function could be written as a loop -- but there are trade-offs. Let's first look at the
obvious. The `fib_loop` function is a bit more complex to read. If needed to write a proof for it, it'd also be
trickier. However, how many "work steps" are we doing? Well, let's dissect it..

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
"""

# A helper function to help us time our `fib` functions.
def time_it(function, val):
    import time
    start_time = time.time()
    function(val)
    time_taken = time.time() - start_time
    print "Time taken for {}({}): {} seconds".format(function.__name__, val, time_taken)


print "Performing time tests!"
time_it(fib_loop, 30) # O(n)
time_it(fib, 30) # O(2^n)


"""
Now, let's write up some other recursive functions. Run this script in order to "test" your implementation. Everything should pass.
These are tricky, so be sure to work out examples by hand and *then* write up your algorithms. If you get stuck, take a step back
and do an example by hand. Try to break the "big" problem into a smaller-sized problem; that's the key to recursion.
"""

def test(actual, expected):
    if actual != expected: print "Uh oh! Expected '{}' but got '{}'".format(expected, actual)

# This function should return the sum of all numbers up to and including `n`.
# TASK: Fix this function using recursion. The tests below should pass.
def sum_up_to_n(n):
    # TODO: Add Base Case
    # TODO: Add Recursive Case
    pass

test(sum_up_to_n(0), 0)
test(sum_up_to_n(1), 1)
test(sum_up_to_n(2), 3)
test(sum_up_to_n(3), 6)
test(sum_up_to_n(4), 10)

# This funciton will "flip" a list using recursion. It might be tempting to cheat with a loop or by using the_list[::-1], but refrain. ;-)
# TASK: Fix this function using recursion. The tests below should pass.
def flip_a_list(the_list):
    # TODO: Add Base Cases -- there should be two, one when the list is empty and one when the list has a single item in it.
    # TODO: Add Recursive Case
    pass

test(flip_a_list([]), [])
test(flip_a_list([1]), [1])
test(flip_a_list([2,1,2]), [2,1,2])
test(flip_a_list([3,2,1]), [1,2,3])

# This function will take a `value_to_add` and a list of numbers. It should return the list where each element has had value_to_add added to it.
# TASK: Fix this function using recursion. The tests below should pass.
def add_to_list(value_to_add, the_list):
    # TODO: Add Base Case
    # Add Recursive Case
    pass

test(add_to_list(1, [0]), [1])
test(add_to_list(1, [1,2]), [2,3])
test(add_to_list(2, [1,2,3]), [3,4,5])

# This function will take a string and determine if it is recursive or not. If it is, it should return True; if not, return False.
# TASK: Fix this function using recursion. The tests below should pass.
def is_palindrome(string):
    # TODO: Add Base Case
    # TODO: Add Recursive Case
    pass

test(is_palindrome(""), True)
test(is_palindrome("t"), True)
test(is_palindrome("cat"), False)
test(is_palindrome("tat"), True)
test(is_palindrome("tacocat"), True)
test(is_palindrome("taco cat"), False)

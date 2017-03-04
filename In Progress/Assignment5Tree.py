"""
Trees are pretty cool data structures. The basic idea with a Tree
is that it is a node that points to multiple different nodes, each 
of which may point to additional nodes. Notice the diagram below.
Node A points to two different nodes, B and C. Node B then points
to nodes D and E; while Node C points to nodes F and G. 
 A 
/ \
 B C
 / | | \
DE FG
Oftentimes it is helpful to think of nodes in a Tree structure
as if they were in a family tree. For example, pretend Node 
A is a grandparent and both nodes B and C are its children.
Based on this relationship, Nodes D-G are all the grandchildren
of Node A. One crucial point is that we can't have nodes pointing
back *up* the Tree at previous nodes. In a family tree, this makes
sense: Node C can't be its own descendant.
It's important to note the recursive nature of Trees, as it helps us
think about them in the right paradigm. Think about the diagram above.
What would happen if we removed Node A entirely but kept its children?
Well, we'd have two smaller Trees (one rooted at B and one rooted ad C)!
As it turns out, our Binary Tree is composed of some "cargo" (that is,
the "value" that the node holds -- such as the value "A", "B", or "C"), 
some (possibly empty) left Tree, and some (possibly empty) right Tree!
To simplify that: a Tree is just a value with a collection of smaller Trees!
One specialized, but quite common, type of Tree is called the Binary
Tree. Binary Trees are like regular Trees, but they are only allowed 
two possible children (often called the "left" and "right" branches 
of the Binary Tree). How you differentiate the "left" and "right"
branches allows a number of optimizations that we'll explore.
For example, suppose we had a bunch of numbers we wanted to store in a tree.
 1 
/ \
 2 3
 / | | \
45 67
Now, if we wanted to determine if the number "7" was in the list, we'd need to
look through every element and ask, "Are you what I'm looking for?" That results
in an O(n) lookup time, as we have to look up each element. Can we do better?...
Well, let's think: why did we have to look at every element? Well, because we 
weren't sure whether the number "7" was on the "left" or the "right" of the "1".
What if we re-arranged the tree such that all numbers "smaller" than the current
number were on the left while the bigger numbers were on the right?
 4 
/ \
 2 6
 / | | \
13 57
Cool, that should work. Every number to the right of the "current" number is bigger
and the numbers to the left are smaller. So let's look for the number "7" again.
First we have "4". Since "7" is bigger than "4", we'll look towards the right and
forget about everything to the left. That's pretty cool: we just "threw out" half of
the numbers! Now we're at "6", but we're looking for "7": we'll go to the right again.
Now we have "7", which is what we're looking for! Huzzah! So rather than look through
every element of the tree, we were able to throw out half of the problem every step of
the way. This is essentially the definition of O(log n) complexity!
What would happen if we added an "8" to that diagram? Well, we want to maintain our new
left-right ordering, or else we lose the nice O(log n) complexity. So, following the right
we'll reach "7" and see that it has two empty branches we could occupy with the number "8".
However, since 7 is less than 8, we'll put the 8 on the branch to the right.
 4 
/ \
 2 6
 / | | \
13 57
 \
8
It's alright that the left branch is still empty; as long as we maintain the left-right ordering
our tree should be able to operate correctly.
Read this: https://www.tutorialspoint.com/data_structures_algorithms/tree_data_structure.htm
Read the beginning of this: http://www.openbookproject.net/thinkcs/python/english2e/ch21.html
Read this for lots of interesting details: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html
TASK: Fill out the missing methods below to make the tests pass. Use recursion where helpful. You shouldn't
need to modify the tests nor the parameters to any of the functions. 
TASK: Determine the complexity of each of the functions you complete.
"""

class BinaryTree(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

		# Pardon the complexity of this repr. It is just meant to print out the Trees nicely.
	def __repr__(self, level=1):
		indent = "" * level
		left_repr = self.left.__repr__(level = level+1) if self.left else "<NONE>"
		right_repr = self.right.__repr__(level = level+1) if self.right else "<NONE>"
		return "{}\n{}{}\n{}{}".format(self.value, indent, left_repr, indent, right_repr)
		
  #Return True if this BinaryTree has no children, or False otherwise.
	def is_leaf(self):
	  if bool(self.value):
	    if self.left == None or self.right == None:
	      return False
	    else:
	       return True

	# Return the number of elements in the tree.
	def size(self): #TOTAL COMPL: O(n^2)
		#I'm going to traverse this tree in preorder (root 1st then all left branches, then finally all right branches)
		if self.value == None:
			return 0 #COMPL: O(1)
		else:
			if not self.left == None:
			  return 1 + self.left.size() #COMPL: O(n)
			else:
			  return 1
			if not self.left == None:
			  return 1 + self.right.size() #COMPL: O(n)
			else:
			  return 1

# Return the number of elements in the longest branch of the tree.
	def height(self): #TOTAL COMPL: O(log n)
		leftSize, rightSize = self.left.size(), self.right.size() #COMPL: O(1)
		if leftSize >= rightSize: #If they are the same size, it doesnt matter which one gets traversed, so it will arbitrarily be the left path of the root
			return 1 + self.left.height() #COMPL: O(log n)
		elif rightSize > leftSize:
			return 1 + self.right.height() #COMPL: O(log n)
		else:
			return 0 #COMPL: O(1)

# Return True if search_val is contained in this tree's contained values, or False otherwise.
# Implement this recursively with an O(log n) algorithm. Think of your "base" and "recursive" cases.
	def contains(self, search_val): #TOTAL COMPL: O(log n)
		current = self.value
		if current == None:		
			return False #COMPL: O(1)
		if current == search_val:
			return True #COMPL: O(1)
		if search_val <= current:
			self.left.contains(search_val, current=self.left) #COMPL: O(log n)
		if search_val >= current:
				self.right.contains(search_val, current=self.right) #COMPL: O(log n)

# Insert the `val` in this Binary Tree. Think recursively: if the `left` and `right` are
# taken, then we'll need to "pass" the `val` down the tree. Additionally, implement this
# where all the values to the "right" are bigger than the values to the "left" (to allow
# for the O(log n) insert and lookup that we explored in the example above.
	def insert(self, val): #TOTAL COMPL: O(log n)
		if self.value == None:
			self.value = val #COMPL: O(1)
		if val <= self.value:
			#iterate until you reach leaf, then insert val
			if self.left == None: 
				self.left = val #COMPL: O(1)
			else: self.left.insert(val) #COMPL: O(log n)
		if val > self.value:
			#iterate until you reach leaf, then insert val
			if self.right == None:
				self.right = val #COMPL: O(1)
			else: self.right.insert(val) #COMPL: O(log n)


"""
Now let's think about making our Binary Tree more general so that any
node may have as many children as it wants. In other words, the while
each Binary Tree may only have a maximum of two children, the Tree
below should be able to support *any* number of children.
TASK: Fill out the missing methods below to make the tests pass. Use recursion where helpful. You shouldn't
need to modify the tests nor the parameters to any of the functions. 
TASK: Determine the complexity of each of the functions you complete.
"""
class Tree(object):
# DO NOT MODIFY.
	def __init__(self, value, children=None):
		self.value = value
		self.children = children if children else []

# Pardon the complexity of this repr. It is just meant to print out the Trees nicely.
	def __repr__(self, level=1):
		indent = "" * level
		children_repr = " " 
		for child in self.children:
		  children_repr += "\n{}{}".format(indent, child.__repr__(level = level+1))
		  return "{}{}".format(self.value, children_repr)

# Mutate the current tree by adding the `child_tree` to the `children`.
	def add(self, child_tree): #TOTAL COMPL: O(1)
		self.children.append(child_tree) #COMPL: O(1)

	# Return the number of elements in the tree.	
	def size(self): #TOTAL COMPL: O(n^2)
		if self.value == []:
			return 0 #COMPL: O(1)
		else:
			size += 1 #COMPL: O(1)
			if self.children == []:
				return 1 #COMPL: O(1)
			else:
				for c in self.children: #COMPL: O(n)
					return 1 + c.size() #COMPL: O(n)

# Return the number of elements in the longest branch of the tree.
	def height(self): #TOTAL COMPL: O(n^2)
		if self.value == None:
			return 0 #COMPL: O(1)
		if self.children == []:
		  return 1 #COMPL: O(1)
		else:
			for c in self.children: #COMPL: O(n)
				if not c.size == 1:
					return 1 + c.height() #COMPL: O(n)

# Return True if the `search_val` exists somewhere in the tree or False otherwise.
	def contains(self, search_val): #TOTAL COMPL: O(n^2)
		if self.value == search_val:
			return True #COMPL: O(1)
		else:
		  for c in self.children: #COMPL: O(n)
			  if c == search_val:
				  return True #COMPL: O(1)
			  if not c.size == 1:
				  c.contains(search_val) #COMPL: O(n)
		  return False #COMPL: O(1)

# Return the Tree that contains a certain `search_val`. If it doesn't exist, return None.
	def get_by_value(self, search_val): #TOTAL COMPL: O(n^2)
		if bool(self.value.contains(search_val)) == True:
			if self.value == search_val:
				return 1 #Height of tree containing search value COMPL: O(1)
			if not self.children == []:
			  for c in self.children: #COMPL: O(n)
			    if not c == search_val:
			      return 1 + c.get_by_value(search_val) #COMPL: O(n)
		else:
		  return None #COMPL: O(1)

# Return True if this BinaryTree has no children, or False otherwise.
	def is_leaf(self): #TOTAL COMPL: O(1)
		if not self.children == []:
			return False #COMPL: O(1)
		else:
			return True #COMPL: O(1)
		
"""
Below is the test suite for the Tree and BinaryTree classes. You shouldn't need to
modify them, but feel free to add more tests if you find a corner case I missed.
"""

def run_number_tree_tests():
	numbers = BinaryTree(4, 
				BinaryTree(2,
				  BinaryTree(1),
				  BinaryTree(3)), 
				BinaryTree(6,
				  BinaryTree(5), 
				  BinaryTree(7)))
				  
	print("Starting Number Tree tests! Woop woop!")
	assert not numbers.is_leaf()
	assert numbers.size() == 7
	assert numbers.height() == 3
	assert numbers.contains(7)
	assert not numbers.contains(8)
	numbers.insert(8)
	numbers.insert(9)
	assert numbers.contains(9)
	assert numbers.height()==5
	print("Crikey! We passed all the tests, mate!\n")

def run_animal_tree_tests():
	animals = Tree("Animals", children=[
	Tree("Mammals", children=[Tree("Cat"),Tree("Dog"),Tree("Human")]), 
	Tree("Reptiles", children=[Tree("Lizard"),Tree("Godzilla"),Tree("Turtle")]), 
	Tree("Fish", children=[Tree("Dory"), Tree("Nemo"), Tree("Shark")])
	])

	print("Starting Animal Tree tests! Cowabunga!")
	assert animals.contains("Human")
	assert not animals.contains("Steve Buscemi")
	assert animals.size() == 13
	assert animals.height() == 3
	animals.get_by_value("Mammals").add(Tree("Elephant"))
	animals.get_by_value("Human").add(Tree("Steve Buscemi"))
	assert animals.contains("Steve Buscemi")
	assert animals.get_by_value("Steve Buscemi").is_leaf()
	assert animals.contains("Shark")
	assert animals.size() == 15
	assert animals.height() == 4
	print("Yay! All the Animal Tree tests passed!\n")

#run_number_tree_tests()
#run_animal_tree_tests()

# If you're really feeling a challenge, try to implement a Trie: https://en.wikipedia.org/wiki/Trie . ;-)

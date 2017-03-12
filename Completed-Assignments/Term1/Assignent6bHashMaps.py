"""
Because dictionaries are an important built-in data structure in python (and therefore requires no class specification for construction),
I will just make a program that demostrates the uses, methods, and functions that correspond to hash maps.
"""
dict_example = {1:1,2:4,3:9}

#The dict constructor builds dictionaries directly from sequences of key-value pairs
dict_example2 = dict([('two', 2), ('one', 1), ('three', 3)])

#Dict comprehensions are also used to create dictionaries from a key:value expression in the same way as list comprehensions build lists
dict_example3 = {x:x**2 for x in (1,2,3)}

#Keyword arguments are used to specify pairs for simple strings
dict(one=1, two=4, three=9)

#View Objects for Dictionaries
"""
len(dictview)
Return the number of entries in the dictionary.

iter(dictview)
Return an iterator over the keys, values or items (represented as tuples of (key, value)) in the dictionary.

Keys and values are iterated over in an arbitrary order which is non-random, varies across Python implementations, and depends on the dictionary’s history of insertions and deletions. If keys, values and items views are iterated over with no intervening modifications to the dictionary, the order of items will directly correspond. This allows the creation of (value, key) pairs using zip(): pairs = zip(d.values(), d.keys()). Another way to create the same list is pairs = [(v, k) for (k, v) in d.items()].

Iterating views while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries.

x in dictview
Return True if x is in the underlying dictionary’s keys, values or items (in the latter case, x should be a (key, value) tuple).

Keys views are set-like since their entries are unique and hashable. If all values are hashable, so that (key, value) pairs are unique and hashable, then the items view is also set-like. (Values views are not treated as set-like since the entries are generally not unique.) Then these set operations are available (“other” refers either to another view or a set):

dictview & other
Return the intersection of the dictview and the other object as a new set.

dictview | other
Return the union of the dictview and the other object as a new set.

dictview - other
Return the difference between the dictview and the other object (all elements in dictview that aren’t in other) as a new set.

dictview ^ other
Return the symmetric difference (all elements either in dictview or other, but not in both) of the dictview and the other object as a new set.
"""


gradeBook = {"Billy": 90, "Josie": 96, "Holden": 40, "Hermione": 100}
names = gradeBook.keys()
grades = gradeBook.values()
classSize = len(gradeBook)


#Iteration
studentBody = []
rollsheet = {}
for student in names:
	studentBody.append(student)
print(studentBody)

#Keys and values are iterated over in the same order
def listRollSheet():
	list(names)
def listAnonGrades():
	list(grades)

#View objects are dynamic and reflect dict changes
def droppedStudent(name):
	del gradeBook[name]

def rollCall():
	for child in gradeBook:
		present = input(child + ": Is student here? y/n")
		if present == "y":
			here = True
		else:
			here = False
		rollsheet.update({child:here})
	list(rollsheet)

def checkForStudent(student):
	if not student in gradeBook:
		print(student + " is not a part of the student body.")
	else:
		if rollsheet[student] == False:
			print(student + " is absent.")
		else:
			print(student + " is present.")
			
listRollSheet()
listAnonGrades()
droppedStudent("Holden")
rollCall()

checkForStudent("Holden")
checkForStudent("Hermione")
checkForStudent("Billy")
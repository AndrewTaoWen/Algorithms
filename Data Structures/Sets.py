# Set definition examples:
example_set1 = {1, 2, 3}
example_set2 = {'h','e','l','l','o'}

print('example_set1:', example_set1)
print('example_set2:', example_set2) # Notice there is only 1 'l'; Also notice the order of the values outputted
print('--')

singleton_set = {7}
empty_set = set() # this is because {} is reversed for a different feature in python 3.

print('Singleton:', singleton_set)
print('Empty Set:', empty_set)

# Basic Built-in Functions w/ Sets

example_set = set('hello') # set() turns an iterable into a set
print('example_set:', example_set)
print('--')

print('Number of Values:', len(example_set)) # length function
print('Minimum Value:', min(example_set)) # min function
print('Maximum Value:', max(example_set)) # max function
print('--')

# tuple to set
tup = (2,3,5,7)
print('tup to set:', set(tup))

# list to set
array = ['orange']*2 +  ['watermelon', 'apple'] + ['kiwi'] * 10
print('Original Array:', array)
print('list to set:', set(array))

# Membership Example
example_set = set('hello')

print("Membership of: \'h\'", 'h' in example_set)
print("Non-Membership of: \'z\'", 'z' not in example_set)

# Iteration of a Set
example_set = {2,3,5,7,11,13}

for v in example_set:
    print('Values of example_set:', v)

# Adding and Removing Values
languages = set() # empty set initialization

programming_languages = ['C', 'C#', 'Java', 'Python', 'HTML', 'CSS', 'JavaScript', 'Haskell']

for item in programming_languages:
    languages.add(item) # .add() method adds an item to a set

print('Languages set:', languages)
print('--')

languages.discard('HTML') # looks for the target value, if found, it will remove from the set
print('HTML deleted:', languages)

languages.remove('CSS') # remove can be used to delete a value;
# only difference is it will raise an error if the target is not found
print('CSS deleted:', languages)

random_remove = languages.pop() # .pop() method deletes a random value and return the value ... not recommended
print('Randomly Removed value:', random_remove)

languages.clear() # .clear() will empty out a set : output is set()
print('Empty languages:', languages)

# Union Example:
set1 = set('hello')
set2 = set('world')

result = set1 | set2 # | is the union operator ... all the members of both set are combined to a single set
# Recall that: there are no duplicates
print('set1 union set 2:', result)

# Union Example:
set1 = set('hello')
set2 = set('world')

result = set1 & set2 # & is the intersection operator
print('Intersection of set1 and set2:', result)

# Difference Example:
set1 = set('hello')
set2 = set('world')

result1 = set1 - set2 # - is the difference operator ... this is set1 difference set2
result2 = set2 - set1 # set2 difference set1

print('set1 - set2:', result1)
print('set2 - set1:', result2)

# Symmetric Difference Example:
set1 = set('hello')
set2 = set('world')

result = set1 ^ set2 # ^ is the symmetric difference operator

print('Symmetric Difference of:', result)

# Proper Subset Example:
set1 = {1,2,3}
set2 = {1,2,3,4}
set3 = {1,2,3}
set4 = set('hello')

print('Is set1 proper subset of set2?:', set1 < set2) # < is the proper subset operator
print('Is set1 proper subset of set3?:', set1 < set3)
print('Is set1 proper subset of set4?:', set1 < set4)

# Subset Example:
set1 = {1,2,3}
set2 = {1,2,3,4}
set3 = {1,2,3}
set4 = set('hello')

print('Is set1 a subset of set2?:', set1 <= set2) # <= is the subset operator
print('Is set1 a subset of set3?:', set1 <= set3) # Notice the difference in value here
print('Is set1 a subset of set4?:', set1 <= set4)

# Superset Example:
set1 = {1,2,3,4}
set2 = {1,2,3,4}
set3 = {1,2,3}
set4 = set('hello')

print('Is set1 proper superset of set2?:', set1 > set2) # > is the proper superset operator
print('Is set1 proper superset of set3?:', set1 > set3)
print('Is set1 proper superset of set4?:', set1 > set4)

# Superset Example:
set1 = {1,2,3,4}
set2 = {1,2,3,4}
set3 = {1,2,3}
set4 = set('hello')

print('Is set1 superset of set2?:', set1 >= set2) # >= is the proper superset operator
print('Is set1 superset of set3?:', set1 >= set3)
print('Is set1 superset of set4?:', set1 >= set4)

# Disjoint Example
# .isdisjoint() is a set method to check for such property between two sets.

set1 = {1,2,3,4}
set2 = {5,6,7}
set3 = {1,2,3,4,5}

print('set1 intersect set2:', set1 & set2) # Output is an empty set
print('set1 intersect set3:', set1 & set3) # Output is an non-empty set
print('--')
print('set 1 disjoint set 2 check:', set1.isdisjoint(set2)) # Therefore .isdisjoint() evaluates to True
print('set 1 disjoint set 3 check:', set2.isdisjoint(set3))

# Union
a = set('abracadabra')
b = set('alacazam')

a.union(b)
print('Union:', a)

# Intersection
a = set('abracadabra')
b = set('alacazam')

a.intersection(b)
print('Intersection:', a)

# Difference
a = set('abracadabra')
b = set('alacazam')

a.difference(b)
print('Difference:', a)

# Symmeteric Difference
a = set('abracadabra')
b = set('alacazam')

a.symmetric_difference(b)
print('Symmetric Difference:', a)

# Subset
a = set('abracadabra')
b = set('alacazam')

print('Subset:', a.issubset(b))

# Superset
a = set('abracadabra')
b = set('alacazam')

print('Superset:', a.issuperset(b))
print('--')

# There are no proper subset/superset methods

# copy
a = set('abracadabra')
b = a.copy()
c = a

a.add('z')
print('.copy() examples:')
print('set a:', a)
print('set b:', b)
print('set c:', c)

# Union and Update --> Update the set, adding elements from all others.
a = set('abracadabra')
b = set('alacazam')

a |= b # same as: a.update(b)
print('Union Update:', a)

# Intersection and Update --> Update the set, keeping only elements found in it and all others.
a = set('abracadabra')
b = set('alacazam')

a &= b # same as: a.intersection_update(b)
print('Intersection Update:', a)

# Difference and Update --> Update the set, removing elements found in others.
a = set('abracadabra')
b = set('alacazam')

a -= b # same as: a.difference_update(b)
print('Difference Update:', a)

# Symmetric Difference and Update --> Update the set, keeping only elements found in either set, but not in both.
a = set('abracadabra')
b = set('alacazam')

a ^= b # same as: a.symmetric_difference_update(b)
print('Symmeteric Difference Update:', a)

# Set Comprehension Example
def isPalindrome(x):
    ''' isPalindrome() returns True if string X is a palindrome '''
    return x == x[::-1]

nums = list(range(1,10000))
palindromic_set = {num for num in nums if isPalindrome(str(num))}

print('Palindromic Numbers Set from 1 to 10000:')
print(palindromic_set)
# import random

# n = int(input())

# l = [(i, i ** 2, i ** 3) for i in range(1,n)]

# suits = ['Club','Spade','Diamond','Heart']
# ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

# cards = [(i, j) for i in suits for j in ranks]

# for i in range(1000):
#     a = random.randint(0, len(cards)-1)
#     b = random.randint(0, len(cards)-1)
#     cards[a], cards[b] = cards[b], cards[a]

# def countChar(s):
#     freq = {}
#     for i in s:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1

#     return [(i, freq[i]) for i in sorted(freq)]

# print(countChar('hello'))

# n = 1000

# def pali(num):
#     num = str(num)
#     return num[::-1] == num

# l = [i for i in range(1,1000) if pali(i)]
# print(l)

# A = {1,2,3,4,5}
# A.pop()

# l = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]

E = set()
O = set()
# for i in l:
#     L.add(i)


# A = {1,2,3,4,5}
# B = {5,6,7,8,9}

# unique = True

# for i in A:
#     if i in B:
#         unique = False
#         break

# for i in range(1,1000):
#     if i % 2 == 0:
#         E.add(i)
#     else:
#         O.add(i)

# A = set()

S = [0, 1, 2]

pS = set()

# lenPS = 2 ** len(S)

# p(n) = power set of n elements
# p(0) = {{}}
# p(1) = {{}, {1st element}}
# p(n) = p(n-1) + p(n-1).add(n th element)

PS = []

PS.append(set())

for i in range(len(S)):
    newPS = PS.copy()
    for j in PS:
        newJ = j.copy()
        newJ.add(S[i])
        newPS.append(newJ)
    PS = newPS

# d = {'A':1,'B':2,'C':3}

# print(d.get('A'))

# del d['A']

# print(d.get('A', 0))

# students = {'GWSS01': 'Jake', 'GWSS02': 'Audrey'}

# # iterating keys
# for key in students.keys():
# 	print(key)

# # iterating values
# for values in students.values():
# 	print(values)

# for pairs in students.items(): # Looking at key,value pairs
# 	print(pairs)

# For each numbers from 2 to N (N → integer user input)
# Create a key, value pair of its Factors

n = 10

d = {}

for i in range(2, n + 1):
    factors = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            factors.append(j)
            if j != i // j:
                factors.append(i // j)
    d[i] = factors

# def collatz(n, memo):
# if n in memo:
#     return memo[n]

# if n == 1:
#     return 1
# if n % 2 == 0:
#     ne = n // 2
# else:
#     ne = 3 * n + 1

# memo[n] = collatz(ne, memo) + 1

# return memo[n]

# count = 1

# while n != 1:

#     if n % 2 == 0:
#         n /= 2
#     else:
#         n = 3 * n + 1

#     count += 1

# return count

# longest = 0
# longestKey = 0

# memo = {}
# for i in range(1,1000000):
#     count = collatz(i, memo)
#     if count > longest:
#         longest = count
#         longestKey = i

# print(collatz(3, memo))
# print(longestKey, longest)

# Q4a) Write a Python program to sum all the values in a dictionary
# def sumDict(dict):

d = {'A': 1, 'B': 2, 'C': 3}
s = sum(d.values())

# # Q4b) Write a Python program to multiply all the values in a dictionary

# def multiplyDict(dict):
#     total = 1
#     for i in dict.values:
#         s *= i

# Q5a) Create a function that sorts a dictionary by key → Create a sorted list of keys.

# print(sorted(d))

# Q5b) Create a function that sorts a dictionary by value → Create a sorted list of values.

# print(sorted(d.values()))

# Q6) Create a fibonacci sequence using a dictionary


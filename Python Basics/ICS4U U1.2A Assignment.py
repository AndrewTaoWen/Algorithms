#!/usr/bin/env python3
# Andrew Wen
# 349358606
# Thu Oct 21, 2021
# U1.2A - Programming Assignment
# Calculate largest possible consecutive sum of a list using two different PythonPractice

# Version 1
# def largest_sum(seq):
#     '''
#     Using nested loops find maximum sum from all possible combinations of sub list
#     Time Complexity: O(n^2)
#     '''

#     lenSeq = len(seq)
#     maxSum = float('-inf')

#     for start in range(lenSeq):
#         for end in range(start , lenSeq + 1):
#             curSum = sum(seq[start : end])

#             if curSum > maxSum:
#                 maxSum = curSum
#         # end of for
#     # end of for

#     return maxSum


# Version 2
def largest_sum(seq):
    '''
    Dynamic programming algorithm. Time Complexity: O(n)
    Define sub problem maxSublistSum[i] as maximum sum of all possible sub list from item 0 to i, INCLUDING i. Then we have sub problem transition function:
        maxSublistSum[i] = max(maxSublistSum[i-1] , 0) + seq[i]
    Which means when calculating the current term of maxSublistSum, we only add the previous term of maxSublistSum if it is positive, otherwise, we start over with seq[i].
    '''

    lenSeq = len(seq)
    maxSublistSum = []

    # Base case: maxSublistSum[0] = seq[0]
    maxSublistSum.append(seq[0])
    # Keep track of largest maxSublistSum
    maxSum = maxSublistSum[-1]

    # Iteratively calculate next term of maxSublistSum
    for i in range(1, lenSeq):
        maxSublistSum.append(max(maxSublistSum[i - 1], 0) + seq[i])
        maxSum = max(maxSum, maxSublistSum[-1])

    return maxSum


# Testing Code, do not edit anything below.
from random import seed
from random import randrange

seed(456)
randList = lambda a, b, size: [randrange(a, b) for x in range(size)]

test1 = [-1, 2, 4, -3, 5, 2, -5, 2]  # 10
test2 = randList(-6, 7, 9)
test3 = randList(-8, 9, 10)
test4 = randList(-10, 11, 20)
test5 = randList(-100, 101, 30)
test6 = randList(-100, 101, 60)
test7 = randList(-1000, 1000, 400)
test8 = randList(-500, 501, 1000)

print('Test 1 | First Few Values:', test1[:10])
print('Test 1 | Output:', largest_sum(test1))
print('Test 1 Pass Result:', largest_sum(test1) == 10)
print('-' * 64)
print('Test 2 | First Few Values:', test2[:10])
print('Test 2 | Output:', largest_sum(test2))
print('Test 2 Pass Result:', largest_sum(test2) == 17)
print('-' * 64)
print('Test 3 | First Few Values:', test3[:10])
print('Test 3 | Output:', largest_sum(test3))
print('Test 3 Pass Result:', largest_sum(test3) == 14)
print('-' * 64)
print('Test 4 | First Few Values:', test4[:10])
print('Test 4 | Output:', largest_sum(test4))
print('Test 4 Pass Result:', largest_sum(test4) == 62)
print('-' * 64)
print('Test 5 | First Few Values:', test5[:10])
print('Test 5 | Output:', largest_sum(test5))
print('Test 5 Pass Result:', largest_sum(test5) == 655)
print('-' * 64)
print('Test 6 | First Few Values:', test6[:10])
print('Test 6 | Output:', largest_sum(test6))
print('Test 6 Pass Result:', largest_sum(test6) == 479)
print('-' * 64)
print('Test 7 | First Few Values:', test7[:10])
print('Test 7 | Output:', largest_sum(test7))
print('Test 7 Pass Result:', largest_sum(test7) == 10541)
print('-' * 64)
print('Test 8 | First Few Values:', test8[:10])
print('Test 8 | Output:', largest_sum(test8))
print('Test 8 Pass Result:', largest_sum(test8) == 5768)
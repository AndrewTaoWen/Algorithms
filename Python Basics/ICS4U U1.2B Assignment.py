# Possible Target Sum
# Edit the given function below.
# seq will be assumed as a list
# target will be assumed as an integer
# Your function should return

# Version 1
# def target_sum(seq, target):
#     '''
#     Use nested loops to try all combinations of 2 values
#     Time complexity O(n^2)
#     '''

#     lenSeq = len(seq)
#     count = 0
#     for i in range(lenSeq):
#         for j in range(i+1,lenSeq):
#             if seq[i] + seq[j] == target:
#                 count += 1

#     return count

# Version 2
def target_sum(seq, target):
    '''
    Two pointers algorithm
    Time Complexity: O(n^2), but in most cases when the duplicates in input list are not too frequent, the time complexity is close to O(n).
    '''
    # Initialize low and high pointers to the two ends of the list
    lo = 0
    hi = len(seq) - 1
    counter = 0

    while lo < hi:
        if seq[lo] + seq[hi] > target:
            hi -= 1
        elif seq[lo] + seq[hi] < target:
            lo += 1
        else:
            # handle duplicate values after finding target, count duplicate on low side and high side. Each duplicate on low side can form a new pair with seq[hi], vice-versa.

            loDup = 0  # number of duplicate values on low side
            tempLo = lo  # temporary low pointer
            while tempLo + 1 < hi and seq[tempLo + 1] == seq[lo]:
                tempLo += 1
                loDup += 1

            hiDup = 0  # number of duplicate values on high side
            tempHi = hi  # temporary high pointer
            while tempHi - 1 > lo and seq[tempHi - 1] == seq[hi]:
                tempHi -= 1
                hiDup += 1

            counter += loDup + hiDup + 1
            hi -= 1
            lo += 1

    return counter


# Testing Code, do not edit anything below.
from random import seed
from random import randrange
from random import choice

seed(456)
randList = lambda a, b, size: sorted(list({randrange(a, b) for x in range(size)
                                           }))

t1_seq, t1_target = [2, 4, 6], 6
t2_seq, t2_target = [2, 4, 6, 8], 10
t3_seq, t3_target = [-1, 2, 4, 5, 6, 8, 10, 13], 12
t4_seq, t4_target = randList(1, 30, 12), choice(range(1, 20))
t5_seq, t5_target = randList(1, 50, 30), choice(range(15, 50))
t6_seq, t6_target = randList(-100, 101, 30), choice(range(40, 200))
t7_seq, t7_target = randList(-10, 1001, 120), choice(range(100, 1000))

print('Test 1 | First Few Values:', t1_seq[:10], 'Target:', t1_target)
print('Test 1 | Output:', target_sum(t1_seq, t1_target))
print('Test 1 Pass Result:', target_sum(t1_seq, t1_target) == 1)
print('-' * 64)
print('Test 2 | First Few Values:', t2_seq[:10], 'Target:', t2_target)
print('Test 2 | Output:', target_sum(t2_seq, t2_target))
print('Test 2 Pass Result:', target_sum(t2_seq, t2_target) == 2)
print('-' * 64)
print('Test 3 | First Few Values:', t3_seq[:10], 'Target:', t3_target)
print('Test 3 | Output:', target_sum(t3_seq, t3_target))
print('Test 3 Pass Result:', target_sum(t3_seq, t3_target) == 3)
print('-' * 64)
print('Test 4 | First Few Values:', t4_seq[:10], 'Target:', t4_target)
print('Test 4 | Output:', target_sum(t4_seq, t4_target))
print('Test 4 Pass Result:', target_sum(t4_seq, t4_target) == 1)
print('-' * 64)
print('Test 5 | First Few Values:', t5_seq[:10], 'Target:', t5_target)
print('Test 5 | Output:', target_sum(t5_seq, t5_target))
print('Test 5 Pass Result:', target_sum(t5_seq, t5_target) == 6)
print('-' * 64)
print('Test 6 | First Few Values:', t6_seq[:10], 'Target:', t6_target)
print('Test 6 | Output:', target_sum(t6_seq, t6_target))
print('Test 6 Pass Result:', target_sum(t6_seq, t6_target) == 0)
print('-' * 64)
print('Test 7 | First Few Values:', t7_seq[:10], 'Target:', t7_target)
print('Test 7 | Output:', target_sum(t7_seq, t7_target))
print('Test 7 Pass Result:', target_sum(t7_seq, t7_target) == 1)
print('-' * 64)

# copy the following below my testing code
from random import seed
from random import randrange
from random import choice

seed(218)
randList2 = lambda a, b, size: sorted([randrange(a, b) for x in range(size)])

t8_seq, t8_target = randList2(-10, 11, 12), choice(range(1, 15))
t9_seq, t9_target = randList2(-100, 101, 150), choice(range(50, 200))
t10_seq, t10_target = randList2(-10000, 10001, 10000), choice(range(5000, 20000))

print('Test 8 | First Few Values:', t8_seq, 'Target:', t8_target)
print('Test 8 | Output:', target_sum(t8_seq, t8_target))
print('Test 8 Pass Result:', target_sum(t8_seq, t8_target) == 3)
print('-' * 64)
print('Test 9 | First Few Values:', t9_seq[:10], 'Target:', t9_target)
print('Test 9 | Output:', target_sum(t9_seq, t9_target))
print('Test 9 Pass Result:', target_sum(t9_seq, t9_target) == 36)
print('-' * 64)
print('Test 10 | First Few Values:', t10_seq[:10], 'Target:', t10_target)
print('Test 10 | Output:', target_sum(t10_seq, t10_target))
print('Test 10 Pass Result:', target_sum(t10_seq, t10_target) == 1223)
print('-' * 64)
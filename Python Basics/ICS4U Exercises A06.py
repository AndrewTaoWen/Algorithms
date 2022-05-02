# A6A: Create a list of even numbers

# num = int(input())

# list_Even = []

# for i in range(num):
#     if i % 2 == 0:
#         list_Even.append(i)

# print(list_Even)

# A6B:  Create a list of characters in a string

# string = list(input())

# print(string)

# A6C: List of Factors
# n = int(input())

# factors = []

# for i in range(1, int(n ** 0.5)+1):
#     if n % i == 0 and n // i != i:
#         factors.append(i)
#         factors.append(int(n/i))

# print(sorted(factors))

# A6D: List of Random Numbers

# from random import seed
# from random import randint

# lim_min = int(input('Enter min '))
# lim_max = int(input('Enter max '))
# num = int(input())

# seed(1)

# rand_nums = []

# for _ in range(num):
#     rand_nums.append(randint(lim_min, lim_max))

# print(rand_nums)

# A6E: Compare two Lists
# list1 = list(input())
# list2 = list(input())

# new_list = []

# for j in list1:
#     if j in list2:
#         new_list.append(j)
#         list1.remove(j)

# print(new_list)

# A6F: List of Prime Numbers under N
# num = int(input())

# for i in range(1, num):
#     for k in range(2,i):
#         if i % k == 0:
#             break
#     else:
#         print(i)

# A6G: Remove Duplicates
# input_list = set(input())

# new_list = []

# for i in input_list:
#     if i not in new_list:
#         new_list.append(i)

# print(new_list)

# A6H: Collatz Sequence
# n = int(input())

# collatz = []

# while n != 1:

#     collatz.append(n)

#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = n * 3 + 1
# collatz.append(1)

# print(collatz)

# A6I: Fibonacci Numbers
# num = int(input())

# fib = [0,1]

# for i in range(2,num+1):
#     fib.append(fib[i-1] + fib[i-2])

# print(fib)

# A6J: Statistics

# u_input = input()

# list_input = []

# while u_input:
#     list_input.append(int(u_input))

#     u_input = input()


# print('Mean:', sum(list_input)/len(list_input))

# occurances = {}

# for i in list_input:
#     if i not in occurances:
#         occurances[i] = 0
#     else:
#         occurances[i] += 1

# most_occurance = 0
# most = 0

# for i in occurances:
#     if occurances[i] > most_occurance :
#         most_occurance = occurances[i]
#         most = i

# print('Mode:', most)

# print('Median:', list_input[len(list_input)//2])

# largest = 0

# for i in range(999,100,-1):
#     for k in range(999,100,-1):
#         l = i*k
#         l_reversed = str(l)[::-1]
#         if str(l) == l_reversed:
#             if l > largest:
#                 largest = l

# print(largest)





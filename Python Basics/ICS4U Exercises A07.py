# A7.a Create an even number checking function

# def even(num):
#     iseven = False

#     if num % 2 == 0:
#         return True

#     return iseven

# A7.b Create a Palindrome checking Function

# def palindrome(string):
#     ispalindrome = False

#     if string[::-1] == list(string):
#         isplaindrome = True

#     return ispalindrome

# A7.c Create a Prime Number checking Function

# num = int(input())

# def prime(num):
#     isprime = False

#     for i in range(2,int(num**0.5+1)):
#         if num % i == 0:
#             break
#     else:
#         isprime = True

#     return isprime

# print(prime(num))

# A7.d Create a Vowel Counting Function

# def vowelCounter(string):

#     count = 0

#     for i in string.lower():
#         if i in 'aeiou':
#             count += 1

#     return count

# A7.e Create a Factorial Calculator

# num = int(input())

# def factorial(num):

#     fact_num = 1

#     for i in range(1,num+1):
#         fact_num *= i

#     return fact_num

# print(factorial(num))

# A7.f Create a Nth Prime Number finding function

# num = int(input())

# def find_prime(num):

#     i = 1

#     count = 1

#     while count <= num:

#         i += 1

#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 break
#         else:
#             count += 1


#     return i

# print(find_prime(num))

# A7.g Create a Searching Function

# data = input()
# target = input()

# def search(data, target):

#     for i in range(len(data)):
#         if data[i] == target:
#             return i
#             break
#     else:
#         return -1

# print(search(data,target))

# A7.h Create a function that returns a list of factors of a number

# num = int(input())

# def list_factors(num):

#     factors = []

#     for i in range(1,int(num ** 0.5)):
#         if num % i == 0:
#             factors.append(i)
#             factors.append(num // i)

#     return factors

# print(list_factors(num))

# A7.i Nth Fibonacci Number Function

num = int(input())


def fibN(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibN(num - 1) + fibN(num - 2)


print(fibN(num))
# Exercise A: Fancy Name Output
# name = input()

# for i in range(len(name)):
#     print(name[:(len(name))-i])

# Exercise B: String Manipulation Exercises
# P1
# num = int(input())

# for i in range(1,num+1):
#     print(str(i)*i)
# P2
# num = int(input())

# for i in range(1,num+1):
#     print('*' * i)

# for i in range(num-1,0,-1):
#     print('*' * i)

# Exercise C: String Manipulation Exercises continued
# num = int(input())

# pattern = ''

# for i in range(1, num+1):
#     if i % 2 == 0:
#         pattern += '0'
#     else:
#         pattern += '1'
#     print(pattern)

# Exercise D: Palindrome
# word = input()

# reversed_word = ''

# for i in range(len(word)-1,-1,-1):
#     reversed_word += word[i]

# print('Palindrome?')
# print(word == reversed_word)

# Exercise E: Sort a String ** hard
# P1
# word = input().lower()

# word_sorted = []

# lowest = 'z'

# for i in word:
#     if i < lowest:
#         word_sorted.insert(0,i)
#         lowest = i
#     else:
#         word_sorted.append(i)

# print(''.join(word_sorted))

# P2
# word = input()

# p1 = ''
# p2 = ''

# for i in word:
#     if i in 'aeiou':
#         p1 += i
#     else:
#         p2 += i

# print(p1 + p2)

# P3

# word = list(input().lower())

# word_sorted = []

# while word:
#     max_word = word[0]
#     for i in word:
#         if i > max_word:
#             max_word = i
#     word_sorted.append(max_word)
#     word.remove(max_word)

# print(''.join(word_sorted))

# Anagram
# string1 = input()
# string2 = input()

# if sorted(string1) == sorted(string2):
#     print('is anagram')
# else:
#     print('not anagram')

# Exercise G: Dressing Up 2001

# num = int(input())

# for i in range(1, num+1, 2):
#     print('*' * i + ' ' * 2 * (num - i) + '*' * i)

# for i in range(num-2, 0, -2):
#     print('*' * i + ' ' * 2 * (num - i) + '*' * i)
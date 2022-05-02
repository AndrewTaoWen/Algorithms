#A1a.
f_n = input()
l_n = input()
print('hello ' + f_n + ' ' + l_n + '!')

#A1b
b_y = int(input())
c_y = int(input())

print('you age is ' + (c_y - b_y))

#A1c
t = float(input())
print('in farenheit this is ' + str((t-32)/1.8))

#A1d
num = int(input())

print((num ** 0.5) % 1 == 0)

#A1e
str1 = input()
str2 = input()
print(str1 in str2)

#A1f
user_input = input()
print(len(user_input))

#A1g
num = int(input())
print((num + 2) % 10 == 0 or (num - 2) % 10 == 0)

#A1h
num = 0.021 * int(input())

if num > 10:
    print(num)
else:
    print(10)

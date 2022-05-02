from random import randrange

#A2a
num = int(input())

if (num ** 0.5) % 1 == 0:
    print(str(num) + ' is a perfect square')
else:
    print(str(num) + ' is a not perfect square')

#A2b
str1 = input()
str2 = input()

if str1 in str2:
    print('yes')
else:
    print('no')

#A2c
num = int(input())

if (num + 2) % 10 == 0 or (num - 2)
 % 10 == 0:
 print('yes')
else:
    print('no')

#A2d
num1 = int(input())
num2 = int(input())

if num1 > num2:
    print('first num is bigger')
else:
    print('second num is bigger')

#A2e
num = 0.021(float(input()))

if num < 10:
    print('10')
else:
    print(num)

#A2f
#part b
grade_List = []

for i in range(4):
    grade_List.append(float(input()))

av_grades = sum(grade_List)/len(grade_List)

if av_grades >= 80:
    print('higher or equal to 80 average')
    if 94 >= av_grades >= 90:
        print('$2000 dollar scholarship')
    elif 100 >= av_grades >= 95:
        print('$4000 scholarship')
        rand_num = randrange(1,11)
        if rand_num == 10:
            print('10% chance of getting a full ride scholarship')
else:
    print('lower than 80')

#A2g Part A & B
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Equilateral Triangle')
elif (a + b > c) or (a + c > b) or (b + c > a):
    if a != b != c:
        print('Scalene Triangle')
    else:
        print('Isoceles')
else:
    print('no triangle can be made')

#A2i
age = int(input())


if age > 18:
    print('can watch movies of all ratings')
elif 13 <= age:
    print('can enjoy all movies except a rating of r')
else:
    print('will require parental guidance for PG-13 while watching the rest')
print('All ages can enjoy g rated movies')

#A2j
user_input = int(input())

if num % 2 != 0:
    print('Weird')
else:
    if 6 <= num <= 20:
        print('weird')
    else:
        print('Not Weird')

#A2k
record = []

for i in range(6):
    record.append(input())

wins = record.count('W')

if wins >= 5:
    print('1')
elif wins >= 3:
    print('2')
elif wins >= 1:
    print('3')
else:
    print('-1')


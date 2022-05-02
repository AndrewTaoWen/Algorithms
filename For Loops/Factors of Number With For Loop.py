# user_input = 0

# while user_input <= 0:

#   user_input = int(input())

# for i in range(1, user_input+1):
#   if user_input % i == 0:
#     print(i)

num = int(input(''))

for i in range(1, num + 1):
    if num % i == 0:
        print(i, 'is a factor of:', num)

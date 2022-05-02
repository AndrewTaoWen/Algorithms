# user_input = input()

# print(user_input)
# for i in range(-1, -1*len(user_input), -1):
#   print(user_input[:i])

num = int(input('Enter a value of N:'))

# for i in range(num+1):
#   print('*'*i)
# for i in range(num-1,1,-1):
#   print('*'*i)

for i in range(num + 1):
    output = ''
    for k in range(1, num + 1):
        if k % 2 == 0:
            output += '0'
        else:
            output += '1'
    print(output[:i])

# pattern = ''
# for i in range(1, num+1):
#   if i % 2 == 0:
#     pattern += '0'
#   else:
#     pattern += '1'

#   print(pattern)

# print('-----')
# pattern2 = '10' * num
# print(pattern2)
# for i in range(1, num +1):
#   print(pattern2[:i])

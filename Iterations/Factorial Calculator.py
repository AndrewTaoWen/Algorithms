# user_input = int(input())

# factorial = 1

# for i in range(user_input, 0, -1):
#   factorial *= i

# print(factorial)

num = int(input())

factorial = 1
start = num

while start > 0:
  factorial *= start

  start -= 1

print('The result is: ', factorial)
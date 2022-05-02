# user_input = input()

# digSum = 0

# for i in user_input:
#   digSum += int(i)

# steps = 0
# sDigSum = 0

# for i in str(digSum):
#   if sDigSum <= 10:
#      sDigSum += int(i)
#   steps += 1

# print(steps)

num = int(input())

step = 0

start = num

while len(str(num)) != 1:

  total = 0

  for digit in str(num):
    total += int(digit)

  num = total

  step += 1

print(start, 'took', step, 'steps to become single digit')
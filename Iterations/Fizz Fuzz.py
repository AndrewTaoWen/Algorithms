# for i in range(1,51):
#   if i % 15 == 0:
#     print('Fizz Buzz')
#   elif i % 3 == 0:
#     print('Fizz')
#   elif i % 5 == 0:
#     print('Buzz')
#   else:
#     print(i)

start = 1
while start <= 50:
  if start % 15 == 0:
    print('FizzBuzz')
  elif start % 3 == 0:
    print('Fizz')
  elif start % 5 == 0:
    print('Buzz')
  else:
    print(start)
  start += 1
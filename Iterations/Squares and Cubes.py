user_input = int(input())

# for i in range(2, user_input+1):
#   print(i ** 2, i ** 3)

start = 2

while start <= user_input:
  print(start, start ** 2, start ** 3)

  start += 1

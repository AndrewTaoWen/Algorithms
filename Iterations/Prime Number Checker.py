user_input = int(input())

# for i in range(1, user_input):
#   for k in range(2, i):
#     if i % k == 0:
#       break
#   else:
#     print(i)

start = 2

while start <= user_input:

  num = start

  divider = 1
  factor_counter = 0

  while divider <= num:
    if num % divider == 0:
      factor_counter += 1
    divider += 1

  if factor_counter == 2:
    print(num,'is prime number.')

  start += 1


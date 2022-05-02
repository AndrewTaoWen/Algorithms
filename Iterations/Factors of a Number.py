user_input = int(input())

# for i in range(1, user_input+1):
#   if user_input % i == 0:
#     print(i)

divider = 1
while divider <= user_input:
  if user_input % divider == 0:
    print(divider)

  divider += 1
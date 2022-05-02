user_input = int(input())

total_sum = 0

# for i in range(user_input+1):
#   total_sum += i

# print(total_sum)

start = 1

while start <= user_input:
  total_sum += start

  start += 1

print('the total sum is', total_sum)
user_input = int(input())
# numbers = []

# for i in range(1, user_input+1):
#   if i % 5 == 0 or i % 3 == 0:
#     numbers.append(i)

# print(sum(numbers))

total_sum = 0
start = 1
while start <= user_input:
    if start % 3 == 0 or start % 5 == 0:
        total_sum += start

    start += 1

print(total_sum)

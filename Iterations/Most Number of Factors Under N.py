# user_input = int(input())

# most_factors = 0
# counter = 0

# for i in range(1, user_input):
#   temp_counter = 0
#   for k in range(1,i):
#     if i % k == 0:
#       temp_counter += 1
#   if temp_counter >= counter:
#     most_factors = i


# print(most_factors)

upper_limit = int(input())

max_count = 0

result = 0

start = 1

while start <= upper_limit:

    num = start

    divider = 1

    factor_count = 0

    while divider <= num:
        if num % divider == 0:
            factor_count += 1

        divider += 1

    if factor_count > max_count:
        max_count = factor_count
        result = start

    start += 1

print(result, 'had the most factors.')
print(result, 'had', max_count, 'factors.')

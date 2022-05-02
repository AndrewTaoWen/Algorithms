# num1 = int(input())
# num2 = int(input())
# num1_factors = []
# num2_factors = []

# for i in range(1,num1):
#   if num1 % i == 0:
#     num1_factors.append(i)

# for i in range(1, num2):
#     if num2 % i == 0 and i in num1_factors:
#       print(i)

num_a = int(input())
num_b = int(input())

divider = 1

upper_limit = min(num_a, num_b)

while divider <= upper_limit:
    if num_a % divider == 0 and num_b % divider == 0:
        print(num_a, 'and', num_b, 'share the factor of', divider)

    divider += 1
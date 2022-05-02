# num = int(input())

# factorial = 1

# for i in range(1, num+1):
#   factorial *= i

# print(factorial)

# #while loop setattr

# num_mult = 1
# fact2 = 1

# while True:
#   num_mult += 1

#   fact2 *= num_mult

#   if num_mult == num:
#     break


# print(fact2)

num = int(input())

num1 = num
num2 = num

product = 1

while num1 > 0:
    product *= num1
    num1 -= 1

print('The factorial of,', num, 'is', product)

productF = 1

for value in range(num2, 0, -1):
    productF *= value

print('The factorial of', num, 'is', productF)
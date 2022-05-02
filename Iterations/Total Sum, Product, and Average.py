flag = 0
user_inputs = []

first_Num = float(input())

product = first_Num

while flag < 9:
    x = float(input())

    user_inputs.append(x)
    product *= x

    flag += 1

user_inputs.insert(0, first_Num)

print('sum is', sum(user_inputs))
print('average is', sum(user_inputs) / 10)
print('total product is', product)
import timeit

start = timeit.default_timer()

num = int(input('Enter a value: '))

factor_list = []

for divider in range(1, int(num ** 0.5)):
    if num % divider == 0:
        factor_list.append(divider)
        factor_list.append(num//divider)

factor_list.append(num)

print(factor_list)

stop = timeit.default_timer()

print('Time: ', stop - start)
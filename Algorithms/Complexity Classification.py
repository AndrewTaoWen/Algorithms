# def factor_counter(n):
#     ctr = 0
#     for divisor in range(1, n+1):
#         if n % divisor == 0:
#             ctr += 1

#     return ctr
num = int(input())


def factor_counter(n):
    ctr = 0
    if n < 9:
        for divisor in range(1, n + 1):
            if n % divisor == 0:
                ctr += 1
        return ctr
    else:
        end = int(n ** 0.5) + 1

        for divisor in range(1, end):
            if n % divisor == 0 and (n // divisor) != divisor:
                ctr += 2
            # second condition ensures that divisor is not added twice
            elif n % divisor == 0 and (n // divisor) == divisor:
                ctr += 1
    return ctr


print(factor_counter(num))
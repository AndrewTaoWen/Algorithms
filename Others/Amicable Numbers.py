# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.


def factors(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != 1:
                factors.append(n // i)

    return set(factors)


# for i in range(1,1000):

sumA = 0

for i in range(1, 10000):
    m = sum(factors(i))
    if i == sum(factors(m)) and i != m:
        sumA += i
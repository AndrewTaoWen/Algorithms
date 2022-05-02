# Dictionary Exercises
# Oct 20, 2021

def findFactors(n):
    factors = []
    for i in range(1 , int(n ** 0.5)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)

    return set(factors
    )

n = int(input())

d = {}

for i in range(2, n+1):
    d[i] = findFactors(i)

print(d)



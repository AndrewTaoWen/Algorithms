# n = 28123

def factors(n):
    factors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            if i != 1:
                factors.add(n // i)

    return factors


abundent = []
for i in range(1, 28123):
    if sum(factors(i)) > i:
        abundent.append(i)

lenA = len(abundent)
print(lenA)
sumAbun = []

cnt = 0
for i in range(lenA):
    for j in range(i, lenA):
        cnt += 1
        # sumAbun.append(abundent[i]+abundent[j])
# print(len(sumAbun))
# s = 0
# for i in range(25, 28123):
#     if i not in sumAbun:
#         s += i

print(cnt)

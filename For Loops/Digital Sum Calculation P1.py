largest = 0
larg_DigSum = 0

for i in range(1, 1001):
  digSum = 0
  for k in str(i):
    digSum += int(k)
  if digSum >= larg_DigSum:
    larg_DigSum = digSum
    largest = i

print(largest)
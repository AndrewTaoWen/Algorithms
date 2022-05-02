maxFib = int(input())
fibSeq = [0, 1]

count = 0

sumEven = 0

while True:
    count += 1
    currentFib = fibSeq[count-1]+fibSeq[count]
    if currentFib > maxFib:
        break
    if currentFib % 2 == 0:
        sumEven += currentFib
    fibSeq.append(currentFib)

print(sumEven)

# print(fib[user_input-1])

# num = int(input())

# if num == 0:
#   print('Fib at', num, 'is', 0)
# elif num == 1:
#   print('fib at', num, 'is', 1)
# else:
#   fib_0 = 0
#   fib_1 = 1
#   fib_n = 0

#   nth_location = 2

#   while nth_location <= num:
#     fib_n = fib_0 + fib_1
#     fib_0 = fib_1
#     fib_1 = fib_n

#     nth_location += 1


#   print('fib at', num, 'is' ,fib_n)
# A3a

# num = -1

# while num < 0:
#     num = int(input())

# for i in range(1, round(num ** 0.5)):
#     if num % i == 0:
#         print(i)
#         print(int(num/i))

# A3b

# num = int(input())

# for i in range(2, round(num ** 0.5)+1):
#     if num % i == 0:
#         print('not prime')
#         break
# else:
#     print('prime')

# A3c
# num = int(input())

# for i in range(1, num+1):
#     for k in range(2, round(i ** 0.5)+1):
#         if i % k == 0:
#             break
#     else:
#         print(str(i) + ' prime')

# A3d
# p1
# num = int(input())

# flag = 0
# fact_num = 1

# while flag < num:
#     flag += 1
#     fact_num *= flag

# print(fact_num)

# p2
# num = int(input())

# fact_num = 1

# for i in range(1,num+1):
#     fact_num *= i

# print(fact_num)

# A3e
# num = int(input())
# most_prime = 0
# largest_count = 0

# for i in range(1, num+1):
#     count = 0
#     for k in range(2,round(i ** 0.5)+1):
#         if i % k == 0:
#             count += 2
#     if count >= largest_count:
#         largest_count += count
#         most_prime = i

# print(most_prime, 'has the most factors with', largest_count)

# A3f
n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a = 0
    b = 1
    c = 0
    for i in range(n - 1):
        c += (a + b)
        a = b
        b = c
        c = 0

    print(b)

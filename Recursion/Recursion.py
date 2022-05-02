# Fibonacci Function

num = int(input())
counter = [0]

# def fibonacci(n, count=0):
#     counter[0] += 1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

memo = {}


def fibonacci(n):
    if n in memo:
        return memo[n]
    counter[0] += 1
    if n <= 1:
        return n
    fib = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = fib

    return fib


print(fibonacci(num))

print(counter[0])

# Recursive Sum

# def recursive_sum(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return n + recursive_sum(n-1)

# print(recursive_sum(num))
# end of recursive_sum

# def tail_recursive_sum(n, tail = 0):
#     if n == 0:
#         return tail
#     else:
#         return tail_recursive_sum(n-1, tail+n)

# print(tail_recursive_sum(num))
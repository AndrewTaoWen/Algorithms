import time

start = timer()

num = int(input())


# def sumnum(n):
#     if n == 0:
#         return 0
#     if not n % 2 == 0:
#         return sumnum(n-1)
#     else:
#         return n + sumnum(n-2)

# print(sumnum(num))

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(num))

end = timer()
print(end - start)

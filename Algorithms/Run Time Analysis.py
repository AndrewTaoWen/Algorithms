# METHOD #1

# def factor_counter(n):

#     #counter
#     ctr = 0
#     for divisor in range(1,n+1):
#         if n % divisor == 0:
#             ctr += 1

#     return ctr

# from timeit import default_timer as timer

# start_timer = timer() #start timer

# up_lim = 10000
# max_count = 0
# result = 0

# for n in range(1, up_lim):
#     n_ctr = factor_counter(n)

#     if n_ctr > max_count:
#         result = n
#         max_count = n_ctr

# end_timer = timer()

# run_time = end_timer - start_timer

# print('Run Time', run_time)

# METHOD #2
# testing_code = '''
# def factor_counter(n):

#     ctr = 0
#     for divisor in range(1,n+1):
#         if n % divisor == 0:
#             ctr += 1

#     return ctr

# upper_lim = 10000
# max_count = 0
# result = 0

# for n in range(1,upper_lim):
#     n_ctr = factor_counter(n)

#     if n_ctr > max_count:
#         result = n
#         max_count = n_ctr
# '''

testing_code = '''
def factor_counter(n):
    """ factor_counter() determines the number of factors N has """

    ctr = 0
    if n < 9:
        # difference of speed between the optimized and non-optimized is very minimial on small numbers
        for divisor in range(1,n+1):
            if n % divisor == 0:
                ctr += 1

        return ctr
    else:
        end_point = int(n**0.5) + 1

        for divisor in range(1, end_point):
            if n % divisor == 0 and (n // divisor) != divisor:
                ctr += 2
            elif n % divisor == 0 and (n // divisor) == divisor:
                ctr += 1

    return ctr
# end of factor_counter

upper_limit = 10000
max_count = 0
result = 0

for n in range(1,upper_limit):
    n_ctr = factor_counter(n)

    if n_ctr > max_count:
        result = n
        max_count = n_ctr
'''

import timeit as t

run_time = t.timeit(testing_code, number=10) / 10

print('Run Time:', run_time)


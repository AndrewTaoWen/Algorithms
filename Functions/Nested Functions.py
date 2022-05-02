def factors(x):
    ''' factors() return a list of factors for x

    arguments:
    -- x : integer

    return
    -- list
    '''

    def isDivisible(num):
        ''' isDivisible() checks if given num is a factor of x'''

        return x % num == 0
    # end of inner function: isDivisible()


    result = []

    for i in range(1, x+1):
        if isDivisible(i):
            result.append(i)

    return result
# end of factors()

factors_12 = factors(12)
print('The factors of 12 are:', factors_12)

print('Is 12 divisible by 5?:', isDivisible(5)) # Should output an error as function is within

def palindrome(s):
    '''
    No tail recursion implementation of palindrome check.
    After the recursive call return, it needs to do an 'and' operation with s[0] == s[-1] before returning to the previous stack. Since the complier needs to keep the result of s[0] == s[1].
    '''
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and palindrome(s[1:-1])


print("non-tail-recursion test")
print(palindrome(''))
print(palindrome('a'))
print(palindrome('abcba'))
print(palindrome('abcde'))
print(palindrome('hanah'))

# print(palindrome('a' * 2000))

# RecursionError: maximum recursion depth exceeded while calling a Python object

print()


def tail_recursion_palindrome(s):
    '''
    Tail recursion implementation of palindrome check.
    The recursive call is the last step in the recursive function. The compiler
    can potentially optimize the memory usage by discarding previous stack frame because there is nothing to check in previous frame.
    '''
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False;
    return tail_recursion_palindrome(s[1:-1])


print("tail-recursion test")
print(tail_recursion_palindrome(''))
print(tail_recursion_palindrome('a'))
print(tail_recursion_palindrome('abcba'))
print(tail_recursion_palindrome('abcde'))
print(tail_recursion_palindrome('hanah'))

# print(tail_recursion_palindrome('a' * 2000))
# Still having the same error. RecursionError: maximum recursion depth exceeded while calling a Python object

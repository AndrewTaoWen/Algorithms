def r_fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * r_fact(n - 1)


def r_fact_tail(n, tail=1):
    if n == 1 or n == 0:
        return tail
    else:
        return n * r_fact_tail(n - 1)


def exponent1(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * exponent1(base, exponent - 1)


def exp_tail(base, exponent, result=1):
    if exponent == 0:
        return result
    else:
        return exp_tail(base, exponent - 1, result * base)


def rec_pali(word):
    if not word:
        return True
    elif len(word) == 1:
        return True
    elif len(word) == 2:
        return word[0] == word[1]
    else:
        return word[0] == word[-1] and rec_pali(word[1:-1])


def reverse(word):
    if len(word) == 1:
        return word
    elif len(word) == 2:
        word[0], word[1] = word[1], word[0]
        return word
    else:
        return 
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    @staticmethod
    def gcd(a,b):
        while b:
            a, b = b, a%b
        return a

    @staticmethod
    def simplify(a,b):
        divisor = Fraction.gcd(a,b)
        n = a // divisor
        d = b // divisor
        return (n,d)

    # def __add__(self):
        # return self.denominator1, '/', (self.numerator1 + self.numerator2

    def __add__(self, other):
        n = self.numerator*other.denominator + other.numerator*self.denominator
        d = self.denominator*other.denominator
        a,b = Fraction.simplify(n,d)
        return Fraction(a,b)

    def __sub__(self, other):
        n = self.numerator*other.denominator - other.numerator*self.denominator
        d = self.denominator*other.denominator
        a,b = Fraction.simplify(n,d)
        return Fraction(a,b)

    def __mul__(self, other):
        n = self.numerator*other.numerator
        d = self.denominator*other.denominator
        a,b = Fraction.simplify(n,d)
        return Fraction(a,b)



fract1 = Fraction(1,2)
fract2 = Fraction(2,3)
print(fract1 * fract2)
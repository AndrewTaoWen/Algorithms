# OOP Assignment
# Vector Class

import math


class Vector:
    """A vector in R3. Vector has the following properties:

    Attributes:
        x: A float representing x component
        y: A float representing y component
        z: A float representing z component
        m: A float representing magnitude
    """

    def __init__(self, x, y, z):
        """Return a Vector object which has component of *x*, *y*, *z*"""
        self.__x = x
        self.__y = y
        self.__z = z
        self.__m = (self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5

    @property
    def x(self):
        """Return x value of this vector"""
        return self.__x

    @property
    def y(self):
        """Return y value of this vector"""
        return self.__y

    @property
    def z(self):
        """Return z value of this vector"""
        return self.__z

    def __str__(self):
        """Return string representation of this vector"""
        vector = f'({self.__x},{self.__y},{self.__z})'
        return vector

    def __repr__(self):
        """Return the official string representation of this vector"""
        v = f'({self.__x},{self.__y},{self.__z})'
        return v

    @property
    def magnitude(self):
        """Return the magnitude of this vector"""
        return round(self.__m, 2)

    def __sub__(self, v2):
        """Return the difference of this vector and *v2*"""
        v = Vector(self.__x - v2.x, self.__y - v2.y, self.__z - v2.z)
        return v

    def __add__(self, v2):
        """Return the sum of this vector and *v2*"""
        v = Vector(self.__x + v2.x, self.__y + v2.y, self.__z + v2.z)
        return v

    def dot(self, v2):
        """Return dot product of this vector and *v2*"""
        dotProduct = self.__x * v2.x + self.__y * v2.y + self.z * v2.z
        return dotProduct

    def isZeroVector(self):
        """Return true or false for wether or not this vector is a zero vector"""
        if self.__x == 0 and self.__y == 0 and self.z == 0:
            return True
        return False

    def isParallelTo(self, v):
        """Return true or false for wether or not this vector is parallel to vector *v*"""
        if self.__x / v.x == self.__y / v.y == self.z / v.z:
            return True
        return False

    def isColinearTo(self, v):
        """Return true or false for wether or not this vector is colinear to vector *v*"""
        if self.__x / v.__x == self.__y / v.__y == self.z / v.z:
            return True
        return False

    def orthogonal(self, v):
        """Return true or false for wether or not this vector is orthogonal to vector *v*"""
        if Vector(self.__x, self.__y, self.z).dot(v) == 0:
            return True
        return False

    def angleTo(self, v2):
        """Return the angle between this vector and vector *v2*"""
        v1 = Vector(self.__x, self.__y, self.z)
        angle = round(math.degrees(math.acos(v1.dot(v2) / (v1.magnitude * v2.magnitude))), 2)

        return angle

    def multiplyScalar(self, k):
        """Return the scalar multiple of this vector and scalar *k*"""
        v = Vector(k * self.__x, k * self.__y, k * self.z)

        return v

    def cross(self, b):
        """Return the cross product of this vector and vector *b*"""
        a = Vector(self.__x, self.__y, self.z)
        r = Vector((a.y * b.z) - (a.z * b.y), (a.z * b.x) - (a.x * b.z), (a.x * b.y) - (a.y * b.x))

        return r

    def __eq__(self, v1):
        """Return true or false for whether or not two vectors are equal"""
        if self.x == v1.x and self.y == v1.y and self.z == v1.z:
            return True
        else:
            return False

    def __neg__(self):
        """Return the opposite vector of this vector"""
        return Vector(-self.x, -self.y, -self.z)


a = Vector(1, 2, 9)

b = Vector(-2, 3, 4)

print('Vector magnitude:')

print(f"%s's magnitude is %s" % (a, a.magnitude))

print('Vector Addition: a + b')

print(f'%s + %s = %s' % (a, b, a + b))

print('Vector Substruction: a - b')

print(f'%s - %s = %s' % (a, b, a - b))

k = 5

print('Scalar multiplying: ka')

print(f'%s%s = %s ' % (k, a, a.multiplyScalar(5)))

print('Dot product: a . b')

print(f'%s . %s = %s' % (a, b, a.dot(b)))

print('Cross produt: a x b')

print(f'%s . %s = %s' % (a, b, a.cross(b)))

print()

print('Properties of dot produt:')

print('Commuicative property: a . b = b . a')

print(f'%s x %s = %s' % (a, b, a.dot(b)))

print(f'%s x %s = %s' % (b, a, b.dot(a)))

print()

print('Distributive property: a . (b + c) = a . b + a . c')

c = Vector(4, 2, 7)

print(f'%s x (%s + %s) = %s' % (a, b, c, a.dot(b + c)))

print(f'%s x %s + %s x %s = %s' % (a, b, a, c, a.dot(b) + a.dot(c)))

print()

print('Magnitude property: a . a = |a|^2')

print(f'%s . %s = %s' % (a, a, a.dot(a)))

print(f'|%s|^2 = %s' % (a, round(a.magnitude ** 2)))

print()

print('Properties of cross produt:')

print('Anti-communicative property: a x b = - b x a')

print(f'%s x %s = %s' % (a, b, a.cross(b)))

print(f'%s x %s = %s' % (b, a, b.cross(a)))

print()

print('Distributive property: a x (b + c) = a x b + a x c')

c = Vector(4, 2, 7)

print(f'%s x (%s + %s) = %s' % (a, b, c, a.cross(b + c)))

print(f'%s x %s + %s x %s = %s' % (a, b, a, c, a.cross(b) + a.cross(c)))

print()

print('Cross another vector and dot itself: (a x b) . a = 0')

print(f'(%s x %s) . %s) = %s' % (a, b, a, a.cross(b).dot(a)))

print()

print('Vector cross itself: (a x a)')

print(f'(%s x %s) = %s' % (a, a, a.cross(a)))

print()

z = Vector(0, 0, 0)

print('Vector crosses zero vector: a x (0,0,0,)')

print(f'(%s x %s) = %s' % (a, z, a.cross(z)))

print()

d = Vector(8, 4, 14)

print('Cross Collinear: c x d = c x k(c)')

print(f'(%s x %s) = %s' % (c, d, c.cross(d)))

print()

print('Associative property: k(a x b) = (ka) x b = a x (kb)')

print(f'%s(%s x %s) = %s' % (k, a, b, (a.cross(b)).multiplyScalar(k)))
print(f'(%s%s) x %s = %s' % (k, a, b, (a.multiplyScalar(k)).cross(b)))
print(f'%s x (%s%s) = %s' % (a, k, b, a.cross((b.multiplyScalar(k)))))

print()

print('Calculate Area of parallelogram in 3D')

print(f'side 1: %s side 2: %s' % (a, b))
print('area of parallelogram is =', a.cross(b).magnitude)

print()
A = Vector(1, 4, 3)
B = Vector(2, 5, 6)
C = Vector(1, 2, 7)
# C = Vector(2,3,2)

print('volume of parallepiped is:')
print(abs(A.dot(B.cross(C))))
print(abs(B.dot(C.cross(A))))
print(abs(C.dot(A.cross(B))))










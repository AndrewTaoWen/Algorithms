# OOP example
class Dog:

    def __init__(self, given_name):
        self.name = given_name

    def getName(self):
        return self.name


# end of dog class

pup = Dog('Tabasco')
print(pup)


class Person:

    def __init__(self, f_name, l_name, birth_year, ):
        self.first = f_name
        self.last = l_name
        self.birth = birth_year

    def getName(self):
        return self.first + ' ' + self.last

    def getYear(self):
        return self.birth

    def calculateAge(self):
        age = 2021 - self.birth
        return age

    def __str__(self):
        return f"{self.first} is born in {self.birth}"


# end class Person

p1 = Person('Mr.', 'Park', 1992)

p1 = Person('Mr.', 'Park', 1992)
print(p1.getName(), p1.getYear())
print('p1 age:', p1.age)

p2 = Person('Marshall', 'Park', 2020)
print(p2.getName())
print('p2 age:', p2.age)

# p2.age = 10000
# print('p2 age:', p2.age)
# print(p1)

name = input()
last_name = input()
year = int(input())
p3 = Person(name, last_name, year)
print(p3.getName())
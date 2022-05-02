class Student:
    def __init__(self, nameF, nameL, num):
        self.firstName = nameF
        self.lastName = nameL
        self.__studentNumber = num

    def __getStudentNumber(self):
        return self.__studentNumber

    # end of student


s1 = Student('Andrew', 'Wen', '349358606')


class Bear:
    def sound(self):
        print('gror')


class Dog:
    def sound(self):
        print('wof')


# base override magic method

class Dog:
    def __init(self, name):
        self.__name = name

    def __str__(self):
        return 'woof'


# __repr_()
# allows printing in all situations

class Card:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    def __str__(self):
        return "Card Object: %s of %s." % (self.__value, self.__suit)

    def __repr__(self):
        return "%s of %s." % (self.__value, self.__suit)

    # Comparison behaviour
    def __eq__(self, other):
        return self.__value == other.__value

    def __gt__(self, other):
        return self.__value > other.__value

    def __lt__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)


example_card = Card('Spades', 'Ace')
print(example_card)

deck = []
SUITS = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
VALUES = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']

for suit in SUITS:
    for value in VALUES:
        deck.append(Card(suit, value))

card1 = deck[0]
card2 = deck[1]

print('are the cards the same?', card1 == card2)
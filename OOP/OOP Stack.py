class Stack:
    def __init__(self, value=None):
        self.__value = None
        self.__child = None

        if self.__value is None:
            self.__size = 0
        else:
            self.__size = 1

        self.__peekValue = self.__value

        def __str__(self):
            result = '<'

            if self.__child is None:
                return result + '>'

            if self.__child is None:
                result += str(self.__value)


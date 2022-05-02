from random import randrange, randint


class Board:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.__moves = [i + j for i in 'ABC' for j in '012']
        self.__locations = [(i, j) for i in range(3) for j in range(3)]
        self.coordinates = {}
        for i in range(len(self.__moves)):
            key = self.__moves[i]
            value = self.__locations[i]
            self.coordinates[key] = value

        print('Our coordinates dictionary')
        print(self.coordinates)

    def __str__(self):
        line1 = '   A B C\n'
        line2 = '0 [' + '|'.join(self.board[0]) + ']\n'
        line3 = '1 [' + '|'.join(self.board[1]) + ']\n'
        line4 = '2 [' + '|'.join(self.board[2]) + ']\n'

        board_out = 'Tic Tac Toe\n\n' + line1 + line2 + line3 + line4
        return board_out

    def playerMove(self, token):
        invalid = True
        row = ''
        column = ''

        while invalid:
            column = input('Enter coloumn (ABC): ')
            row = input('Enter the row (012): ')
            p_choice = column + row

            if p_choice not in self.__moves:
                print('Invalid Move Choice')
            else:
                temp_location = self.coordinates[p_choice]
                x = temp_location[0]
                y = temp_location[1]
                self.board[x][y] = token
                invalid = False
                self.__moves.remove(p_choice)

    def __repr__(self):
        return self.__str__()

    def cpuMove(self, token):
        from random import choice
        if self.__moves:
            temp_move = choice(self.__moves)
            temp_location = choice(self.__moves)

        x = temp_location[0]
        y = temp_location[1]
        self.board[x][y] = token
        self.__moves.remove(temp_move)

    def validate(self):
        # if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]:
        row1 = self.board[0][0] + self.board[0][1] + self.board[0][2]
        row2 = self.board[1][0] + self.board[1][1] + self.board[1][2]
        row3 = self.board[2][0] + self.board[2][1] + self.board[2][2]

        if row1 == '000' or row2 == '000' or row3 == '000':
            return 1
        elif row1 == 'XXX' or row2 == 'XXX' or row3 == 'XXX':
            return 2

        col1 = self.board[0][0] + self.board[1][0] + self.board[2][0]
        col2 = self.board[0][1] + self.board[1][1] + self.board[2][1]
        col3 = self.board[0][2] + self.board[1][2] + self.board[2][2]

        if col1 == '000' or col2 == '000' or col3 == '000':
            return 1
        elif col1 == 'XXX' or col2 == 'XXX' or col3 == 'XXX':
            return 2

        diag1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
        diag2 = self.board[0][2] + self.board[1][1] + self.board[2][0]

        if diag1 == '000' or diag2 == '000':
            return 1
        elif diag1 == 'XXX' or diag2 == 'XXX':
            return 2

        for row in self.board:
            if ' ' in row:
                return 0
        return -1


game = Board()
game_result = 0

while game_result == 0:
    print(game)
    game.playerMove('0')
    game_result = game.validate()
    print(game)

    if game_result not in [1, 2]:
        game.cpuMove('X')
        game_result = game.validate()
        print(game)




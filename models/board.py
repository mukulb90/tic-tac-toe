__author__ = 'mukul'


from models import VerticalRow, Square, Diagonal, HorizontalRow

class GameBoard(object):
    def __init__(self, row_size, col_size):
        """

        """
        self.squares = []
        self.horizontal_rows = []
        self.vertical_rows = []
        self.diagonals = []

        'Create squares based on size required'
        for i in range(0, row_size * col_size):
            square = Square(i)
            self.squares.append(square)

        'Create horizontal rows which hold references to squares'
        for i in range(0, row_size):
            row = HorizontalRow(i, col_size, self.squares)
            self.horizontal_rows.append(row)

        'Create vertical rows which hold references to squares'
        for i in range(0, row_size):
            row = VerticalRow(i, col_size, self.squares)
            self.vertical_rows.append(row)

        'Create diagonal which hold references to squares'
        for i in range(0, 2):
            diagonal = Diagonal(i, col_size, self.squares)
            self.diagonals.append(diagonal)

    def set(self, row_no, col_no, value):
        horizontal_row = self.getHorizontalRow(row_no)
        horizontal_row.setSquare(col_no, value)
        vertical_row = self.getVerticalRow(col_no)
        # vertical_row.setSquare (row_no, value)
        vertical_row.run()

        for diagonals in self.getDiagonals():
            diagonals.run()

    def getHorizontalRow(self, row_num):
        return self.horizontal_rows[row_num]

    def getVerticalRow(self, col_num):
        return self.vertical_rows[col_num]

    def getDiagonals(self):
        return self.diagonals

    def __str__(self):
        for row in self.horizontal_rows:
            print str(row)
        return ' Tic Tac Toe Board'

    def __repr__(self):
        return self.__str__()













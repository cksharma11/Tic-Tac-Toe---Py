class Board:
    def __init__(self):
        self.board = ['','','','','','','','','']

    def placeSymbol(self, position, symbol):
        self.board[position] = symbol

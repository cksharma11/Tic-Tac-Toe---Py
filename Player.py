class Player:
    def __init__(name, symbol):
        self.name = name
        self.symbol = symbol
        self.moves = []

    def makeMove(position):
        self.moves.append(position)

    def getMoves():
        return self.moves

    def getSymbol():
        return self.symbol
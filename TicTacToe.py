from Board import Board
from Player import Player
from Game import Game

def main():
    board = Board()
    player1Name = raw_input("Enter First Player Name : ")
    player2Name = raw_input("Enter Second Player Name : ")

    player1 = Player(player1Name, "X")
    player2 = Player(player2Name, "O")

    showSymbols(player1Name, player2Name)

    game = Game(player1, player2, board)

    while(game.hasWon() != True or game.isDraw() != True):
        game.printBoard()
        currentPlayerMove = getValidMoveMove(game)

        game.makeMove(currentPlayerMove)
        game.updateCurrentPlayer()

    print(game.getCurrentPlayer().getName() + " has Won!")

def getValidMoveMove(game):
    move = int(raw_input(game.getCurrentPlayer().getName() + "'s turn :"))
    while(game.isPlaceEmpty(move)):
            print("Place is already occupied!")
            move =  getValidMoveMove(game)
    return move

def showSymbols(player1, player2):
    print(player1 + "'s symbol is X")
    print(player2 + "'s symbol is O")

main()
from Board import Board
from Player import Player
from Game import Game

def main():
    board = Board()
    player1 = Player("Chandan", "X")
    player2 = Player("Dheeraj", "O")

    game = Game(player1, player2, board)

    while(game.hasWon() != True):
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

main()
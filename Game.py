from Board import Board
from Player import Player
import numpy as np

class Game:
    def __init__(self, player1,player2, board):
        self.players = [player1, player2]
        self.board = board
        self.winningMoves = [[1,2,3],[4,5,6],[7,8,9,],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]

    def updateCurrentPlayer(self):
        self.players = [players[1]] + [players[0]]

    def getCurrentPlayer(self):
        return self.players[0]

    def makeMove(self,position):
        self.getCurrentPlayer().makeMove(position)
        self.bord.placeSymbol(position, self.getCurrentPlayer().getSymbol())

    def hasWon(self, playerMoves):
        return playerMoves in self.winningMoves

    
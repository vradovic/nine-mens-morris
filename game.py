from board import Board
from tree import *

class Game(object):
    def __init__(self):
        self._winner = None
        self._tokens = '@#'
        self._board = Board()
        self._phase = 1
        self._player_pieces = 9
        self._ai_pieces = 9

    def play(self):
        while self._winner is None:
            # player play
            print(self._board)
            player_move = self.get_player_move()
            self.place_player_piece(player_move)
            # evaluate position
            # cpu play
    
    def get_player_move(self):
        while True:
            try:
                coordinates = int(input("Unesite vaš potez: "))
            except ValueError:
                print("Unos mora biti broj.")
                continue
            if coordinates < 0 or coordinates > 23:
                print("Unos mora biti između 0 i 23.")
                continue
            return coordinates
    
    def is_valid_move(self, coordinates):
        piece = self._board.get_pos(coordinates)
        if self._phase == 1:
            if piece != 'x':
                return False
        return True
    
    def place_player_piece(self, coordinates):
        if self.is_valid_move(coordinates):
            self._board.set_pos(coordinates, '@')
            self._player_pieces -= 1
        else:
            print("Ne možete tu postaviti figuru!")

from board import Board
from tree import *

class Game(object):
    def __init__(self):
        self._winner = None
        self._tokens = "@#"
        self._board = Board()
        self._phase = 1

    def play(self):
        while self._winner:
            # player play
            # evaluate position
            # cpu play
            pass
    
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

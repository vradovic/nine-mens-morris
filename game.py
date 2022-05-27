from board import Board
from tree import *

class Game(object):
    def __init__(self):
        self._winner = None
        self.PLAYER_TOKEN = '@'
        self.AI_TOKEN = '#'
        self._board = Board()
        self._phase = 1
        self._player_pieces = 9
        self._ai_pieces = 9
        self._player_turn = 1 # 1 ako je igrac na potezu, -1 ako je protivnik na potezu

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
                if self._phase == 1:
                    start = None
                    end = int(input("Unesite polje na koje želite da postavite figuru: "))
                else:
                    start = int(input("Unesite figuru koju želite da pomerite: "))
                    end = int(input("Unesite poziciju na koju želite da je pomerite: "))
            except ValueError:
                print("Unos mora biti broj.")
                continue
            if start < 0 or start > 23 or end < 0 or end > 23:
                print("Unos mora biti između 0 i 23.")
                continue
            return (start, end)
    
    def is_valid_move(self, move):
        start, end = move[0], move[1]
        if self._phase == 1:
            # U prvoj fazi validan je svaki potez dokle god polje nije zauzeto
            if self._board[end] != 'x':
                return False
            return True
        else:
            # U drugoj fazi validan je potez ako polje nije zauzeto i ako je polje susedno od startnog polja
            if self._board[end] != 'x' and self._board.is_adjacent_point(start, end) == False:
                return False
            return True

    def make_move(self, move):
        start, end = move[0], move[1]
        if self.is_valid_move(move):
            if self._player_turn == 1:
                self._board[end] = self.PLAYER_TOKEN
            else:
                self._board[end] = self.AI_TOKEN
            self._board[start] = 'x'
            self._player_turn *= -1
        print("Nije moguće odigrati ovaj potez!")

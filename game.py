from board import Board
from tree import *
import random

class Game(object):
    def __init__(self):
        self._winner = None
        self.PLAYER_TOKEN = '@'
        self.AI_TOKEN = '#'
        self._board = Board()
        self._stage = 1 # faza igre, samo prva i druga
        self._player_pieces = 0
        self._ai_pieces = 0
        self._player_turn = 1 # 1 ako je igrac na potezu, -1 ako je protivnik na potezu
    
    def display_board(self):
        print(self._board)
        print("Broj vaših figura:", self._player_pieces)
        print("Broj protivničkih figura:", self._ai_pieces)

    def play(self):
        while self._winner is None:
            self.display_board()
            self.check_stage()
            if self._player_turn == 1:
                move = self.get_player_move()
            else:
                move = self.get_ai_move()
            if self.is_valid_move(move):
                self.make_move(move)
            else:
                print("Neispravan potez!")
    
    def check_stage(self):
        if self._player_pieces == 9: # and self._ai_pieces == 9:
            self._stage = 2
    
    def get_player_move(self):
        while True:
            try:
                if self._stage == 1:
                    start = 0
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
    
    def get_ai_move(self):
        pass
    
    def is_valid_move(self, move):
        start, end = move[0], move[1]
        if self._stage == 1:
            # U prvoj fazi validan je svaki potez dokle god polje nije zauzeto
            if self._board.board_map[end] != 'x':
                return False
            return True
        else:
            # U drugoj fazi validan je potez ako polje nije zauzeto i ako je polje susedno od startnog polja
            if self._board.board_map[start] == 'x' or self._board.board_map[end] != 'x':
                return False
            elif (self._board.board_map[start] == self.PLAYER_TOKEN and self._player_turn != 1) or (self._board.board_map[start] == self.AI_TOKEN and self._player_turn == 1):
                return False
            elif self._board.is_adjacent_point(start, end) == False:
                return False
            return True

    def make_move(self, move):
        start, end = move[0], move[1]
        if self._player_turn == 1:
            self._board.board_map[end] = self.PLAYER_TOKEN
            if self._stage == 1:
                self._player_pieces += 1
        else:
            self._board.board_map[end] = self.AI_TOKEN
            if self._stage == 1:
                self._ai_pieces += 1
        if self._stage == 2:
            self._board.board_map[start] = 'x'
        # self._player_turn *= -1

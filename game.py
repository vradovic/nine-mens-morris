from tracemalloc import start
from board import Board
from tree import *
import random
from copy import deepcopy

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
    
    def display_board(self, last_move):
        print(self._board)
        if last_move is not None:
            if self._stage == 1:
                print(f"Protivnik je odigrao na {last_move[1]}.")
            else:
                print(f"Protivnik je odigrao sa {last_move[0]} na {last_move[1]}.")
        print("Broj vaših figura:", self._player_pieces)
        print("Broj protivničkih figura:", self._ai_pieces)

    def play(self):
        last_move = None
        while self._winner is None:
            self.display_board(last_move)
            self.check_stage()
            move = self.get_player_move()
            if self.is_valid_move(move):
                self._board.set_position(move, self.PLAYER_TOKEN)
            else:
                print("Neispravan potez!")
                continue
            self._player_turn *= -1
            move = self.get_ai_move()
            while not self.is_valid_move(move):
                move = self.get_ai_move()
            self._board.set_position(move, self.AI_TOKEN)
            last_move = move
            self._player_turn *= -1
            if self._stage == 1:
                self._player_pieces += 1
                self._ai_pieces += 1
    
    def check_stage(self):
        if self._player_pieces == 9 and self._ai_pieces == 9:
            self._stage = 2
    
    def get_player_move(self):
        while True:
            try:
                if self._stage == 1:
                    start = None
                    end = int(input("Unesite polje na koje želite da postavite figuru: "))
                else:
                    start = int(input("Unesite figuru koju želite da pomerite: "))
                    end = int(input("Unesite poziciju na koju želite da je pomerite: "))
            except ValueError:
                print("Unos mora biti broj.")
                continue
            if start is not None:
                if start < 0 or start > 23 or end < 0 or end > 23:
                    print("Unos mora biti između 0 i 23.")
                    continue
            elif end < 0 or end > 23:
                print("Unos mora biti između 0 i 23.")
                continue
            return (start, end)
    
    def get_ai_move(self):
        # TODO: Ovde implementirati heuristiku !!!
        start = None
        if self._stage == 2:
            start = random.randint(0, 23)
        end = random.randint(0, 23)
        return (start, end)
    
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
    
    # TODO: Napraviti minimax algoritam
    def minimax(self, position, depth, maximizing):
        pass

                    
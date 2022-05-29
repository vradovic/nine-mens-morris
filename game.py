from tracemalloc import start
from board import Board
import random

class Game(object):
    def __init__(self):
        self._winner = None
        self._PLAYER_TOKEN = '@'
        self._AI_TOKEN = '#'
        self._board = Board()
        self._stage = 1 # faza igre, samo prva i druga
        self._stage_counter = 0 # brojac faze, kad dodje do 9 prelazi u drugu fazu
        self._player_pieces = 9
        self._ai_pieces = 9
        self._DEPTH = 10

    def play(self):
        
        while self._winner is None:

            # Igrac
            print(self._board)
            move = self._get_player_input()
            if not self._is_valid_move(move, self._AI_TOKEN):
                print("Potez nije ispravan.")
                continue
            self._board.set_position(move, self._PLAYER_TOKEN)
            if self._is_mill(move[1], self._PLAYER_TOKEN):
                point = self._get_player_input(True, self._AI_TOKEN)
                self._board.set_position(point, 'x')
                self._ai_pieces -= 1
            if self._is_win():
                break

            # AI
            move = self._minimax(self._board.board_map, self._DEPTH, False)
            self._board.set_position(move, self._AI_TOKEN)
            if self._is_win():
                break

            self._stage_counter += 1
            self._update_stage()

    def _get_player_input(self, mill=False, opposing=None):
        while True:
            try:
                if mill:
                    start = None
                    end = int(input("Izaberite polje na kojem želite da uklonite protivničku figuru: "))
                    if self._board.board_map[end] != opposing:
                        print("Polje mora biti sa protivničkom figurom.")
                        continue
                elif self._stage == 1:
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
    
    def _is_valid_move(self, move, opposing):
        start, end = move[0], move[1]

        if self._stage == 1:
            # U prvoj fazi validan je svaki potez dokle god polje nije zauzeto
            if self._board.board_map[end] != 'x':
                return False
            return True
        else:
            # U drugoj fazi validan je potez ako polje nije zauzeto i ako je polje susedno od startnog polja
            if self._board.board_map[start] == 'x' or self._board.board_map[end] != 'x' or self._board.board_map[start] == opposing or not self._board.is_adjacent_point(start, end):
                return False
            return True
    
    def _is_mill(self, point, token):
        points = [x for x in self._board.mills if point in x]
        for i in points:
            if self._board.board_map[i[0]] == token and self._board.board_map[i[1]] == token and self._board.board_map[i[2]] == token:
                return True
        return False
    
    def _is_win(self):
        if self._player_pieces == 2:
            self._winner = "ai"
            return True
        elif self._ai_pieces == 2:
            self._winner = "player"
            return True
        return False
    
    def _update_stage(self):
        if self._stage_counter == 9:
            self._stage = 2
    
    # TODO: Napraviti minimax algoritam
    def _minimax(self, position, depth, maximizing):
        pass

                    
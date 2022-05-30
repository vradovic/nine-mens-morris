from state import State
from copy import deepcopy

class Game(object):
    def __init__(self):
        self._current_state = State() # Trenutno stanje igre
        self._player_turn = True # True - igrac na potezu, False - racunar na potezu
        self._winner = None # Pobednik
        self._depth = 2 # Dubina na kojoj minimax pretrazuje pozicije
    
    # Minimax algoritam
    # TODO: Implementirati alfa beta rez
    def minimax(self, current_state, depth, max_player):
        if depth == 0 or current_state.is_end():
            return (current_state.evaluate(), current_state)

        if max_player:
            max_eval = float('-inf')
            for state in current_state.get_states('@'):
                evaluation = self.minimax(state, depth - 1, False)
                max_eval = max(max_eval, evaluation[0])
                best_move = (max_eval, state)
            return best_move
        else:
            min_eval = float('inf')
            for state in current_state.get_states('#'):
                evaluation = self.minimax(state, depth - 1, True)
                min_eval = min(min_eval, evaluation[0])
                best_move = (min_eval, state)
            return best_move

    # Glavna metoda igre
    def play(self):
        while self._winner is None:
            if self._player_turn:
                print(self._current_state)
                move = (0, 0)
                inpt = self.get_player_input()
                if inpt[1] <= -1:
                    move = inpt[0]
                else:
                    move = inpt[1]
                if self._current_state.is_mill(move):
                    while True:
                        try:
                            get_mill = int(input("Unesite koju figuru želite da uklonite: "))
                        except ValueError:
                            print("Unos mora biti broj.")
                            continue
                        if get_mill < 0 or get_mill > 23:
                            print("Unos mora biti od 0 do 23.")
                            continue
                        self._current_state.set_position(get_mill, '@')
                        break
                self._player_turn = False
            else:
                best_move = self.minimax(self._current_state, self._depth, False)
                self._current_state = best_move[1]
                self._player_turn = True

    def get_player_input(self):
        valid_moves = self._current_state.get_states('@')
        while True:
            if self._current_state._stage == 1:
                try:
                    move = int(input("Unesite polje: "))
                except ValueError:
                    print("Unos mora biti broj.")
                    continue
                if move < 0 or move > 23:
                    print("Unos mora biti od 0 do 23.")
                    continue
                temp = deepcopy(self._current_state)
                temp.set_position(move, '@')
                is_valid = True
                for board in valid_moves:
                    is_valid = True
                    for i in range(24):
                        if temp._board[i] != board._board[i]:
                            is_valid = False
                            break
                    if is_valid:
                        self._current_state = temp
                        self._current_state._stage_counter += 1
                        if self._current_state._stage_counter == 9:
                            self._current_state._stage = 2
                        break
                if is_valid:
                    return (move, -1)
            else:
                try:
                    start = int(input("Izaberite figuru: "))
                    end = int(input("Izaberite polje: "))
                except ValueError:
                    print("Unos mora biti broj.")
                    continue
                if start < 0 or end < 0 or start > 23 or end > 23:
                    print("Unos mora biti od 0 do 23.")
                    continue
                temp = deepcopy(self._current_state)
                temp.set_position(end, '@')
                temp.set_position(start, 'x')
                is_valid = True
                for board in valid_moves:
                    is_valid = True
                    for i in range(24):
                        if temp._board[i] != board._board[i]:
                            is_valid = False
                            break
                    if is_valid:
                        self._current_state = temp
                        break
                if is_valid:
                    return (start, end)

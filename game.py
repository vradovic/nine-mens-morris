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
        if current_state.is_end():
            if max_player:
                return float('inf'), current_state
            else:
                return float('-inf'), current_state

        if depth == 0:
            return current_state.evaluate(), current_state

        if max_player:
            max_eval = float('-inf')
            best_move = None
            for state in current_state.get_states('@'):
                evaluation = self.minimax(state, depth - 1, False)[0]
                max_eval = max(max_eval, evaluation)
                if max_eval == evaluation:
                    best_move = state
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for state in current_state.get_states('#'):
                evaluation = self.minimax(state, depth - 1, True)[0]
                min_eval = min(min_eval, evaluation)
                if min_eval == evaluation:
                    best_move = state
            return min_eval, best_move

    # Glavna metoda igre
    def play(self):
        for i in range(15):
            best_move = self.minimax(self._current_state, self._depth, True)[1]
            self._current_state = best_move
            best_move = self.minimax(self._current_state, self._depth, False)[1]
            self._current_state = best_move
            print(self._current_state)
            self._current_state.update_stage()
            print(self._current_state._stage_counter)
            print(self._current_state._max_pieces)
            print(self._current_state._min_pieces)

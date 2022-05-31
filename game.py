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
                return float('inf')
            else:
                return float('-inf')

        if depth == 0:
            return current_state.evaluate()

        if max_player:
            max_eval = float('-inf')
            best_move = None
            for state in current_state.get_states('@'):
                evaluation = self.minimax(state, depth - 1, False)
                max_eval = max(max_eval, evaluation)
                if max_eval == evaluation:
                    best_move = state
        else:
            min_eval = float('inf')
            best_move = None
            for state in current_state.get_states('#'):
                evaluation = self.minimax(state, depth - 1, True)
                min_eval = min(min_eval, evaluation[0])
                if min_eval == evaluation:
                    best_move = state
        
        return best_move

    # Glavna metoda igre
    def play(self):
        pass

from state import State

class Game(object):
    def __init__(self):
        self._state = State()
    
    def minimax(self, current_state, depth, max_player):
        if depth == 0 or current_state.is_end():
            return current_state.evaluate()

        if max_player:
            max_eval = float('-inf')
            for state in current_state.get_states('@'):
                evaluation = self.minimax(state, depth - 1, False)
                max_eval = max(max_eval, evaluation)
            return max_eval
        else:
            min_eval = float('inf')
            for state in current_state.get_states('#'):
                evaluation = self.minimax(state, depth - 1, True)
                min_eval = min(min_eval, evaluation)
            return min_eval

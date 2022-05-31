from state import State
from copy import deepcopy

class Game(object):
    def __init__(self):
        self._current_state = State() # Trenutno stanje igre
        self._depth = 2 # Dubina na kojoj minimax pretrazuje pozicije
    
    # Minimax algoritam
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
            pos = current_state
            for state in current_state.get_states('@'):
                evaluation = self.minimax(state[0], depth - 1, False)[0]
                max_eval = max(max_eval, evaluation)
                if max_eval == evaluation:
                    pos, best_move = state
            return max_eval, pos, best_move
        else:
            min_eval = float('inf')
            best_move = None
            pos = current_state
            for state in current_state.get_states('#'):
                evaluation = self.minimax(state[0], depth - 1, True)[0]
                min_eval = min(min_eval, evaluation)
                if min_eval == evaluation:
                    pos, best_move = state
            return min_eval, pos, best_move

    # Glavna metoda igre
    def play(self):
        while True:
            print(self._current_state)

            no_moves = False
            for i in self._current_state.get_all_tokens('@'):
                adj_points = self._current_state._adjacent_points[i]
                if 'x' in adj_points:
                    no_moves = True
                    break
            if no_moves:
                print("Izgubili ste! Nemate vise poteza.")
                break
            last_move = self.get_player_input()
            if self._current_state.is_mill(last_move):
                while True:
                    try:
                        player_input = int(input("MICA! Izaberite protivnicko polje: "))
                    except ValueError:
                        print("Unos mora biti broj.")
                    if player_input not in self._current_state.get_all_tokens('#'):
                        print("Neispravno polje.")
                        continue
                    else:
                        self._current_state.set_position(player_input, 'x')
                        self._current_state._min_pieces -= 1
                        break
            if self._current_state.is_end():
                print("Pobedili ste!")
                break

            no_moves = False
            for i in self._current_state.get_all_tokens('@'):
                adj_points = self._current_state._adjacent_points[i]
                if 'x' in adj_points:
                    no_moves = True
                    break
            if no_moves:
                print("Pobedili ste! Protivnik nema vise poteza.")
                break
            evaluation, pos, best_move = self.minimax(self._current_state, self._depth, False)
            self._current_state = pos
            print("Protivnik je odigrao:", best_move)
            print("Procena:", evaluation)
            if self._current_state.is_mill(best_move):
                print("MICA! Protivnik vam je uzeo figuru.")
            self._current_state.update_stage()

            if self._current_state.is_end():
                print("Protivnik je pobedio!")
                break

    def get_player_input(self):
        if self._current_state._stage == 1:
            while True:
                try:
                    player_input = int(input("Unesite broj polja: "))
                except ValueError:
                    print("Unos mora biti broj.")
                    continue
                move = (None, player_input)
                if player_input < 0 or player_input > 23:
                    print("Neispravan potez.")
                elif not self._current_state.is_valid_move(move, '@'):
                    print("Neispravan potez.")
                else:
                    self._current_state.simulate_move(move, '@')
                    return player_input
        else:
            while True:
                try:
                    start = int(input("Izaberite polje: "))
                    end = int(input("Unesite polje: "))
                except ValueError:
                    print("Unos mora biti broj.")
                    continue
                move = (start, end)
                if start < 0 or end < 0 or start > 23 or end > 23:
                    print("Neispravan potez.")
                elif not self._current_state.is_valid_move(move, '@'):
                    print("Neispravan potez.")
                else:
                    self._current_state.simulate_move(move, '@')
                    return end
                

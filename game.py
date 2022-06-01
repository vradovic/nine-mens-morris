from state import State
from time import time


class Game(object):
    def __init__(self):
        self._current_state = State()  # Trenutno stanje igre
        self._depth = 2  # Dubina na kojoj minimax pretrazuje pozicije
        self._winner = None  # Pobednik
        self._turn = 1  # Igrac na potezu

    # Minimax algoritam
    def minimax(self, current_state, depth, max_player):
        if depth == 0 or current_state.is_end():
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
        while self._winner is None:

            if self._turn == 1:
                print(self._current_state)
                move = self.get_player_move()
                self._current_state.simulate_move(
                    move, self._current_state._MAX_TOKEN)
                if self._current_state.is_mill(move[1]):
                    print("Dobili ste micu!")
                    self.handle_mill()
                if self._current_state.is_end():
                    self._winner = self._current_state._MAX_TOKEN
                self._turn *= -1
            else:
                start = time()
                evaluation, position, best_move = self.minimax(self._current_state, self._depth, False)
                end = time()
                elapsed = end - start
                self._current_state = position
                print("Protivnik je odigrao:", best_move)
                print("Proteklo vreme:", elapsed)
                print("Procena trenutne pozicije:", evaluation)
                if self._current_state.is_mill(best_move[1]):
                    print("Protivnik je dobio micu.")
                if self._current_state.is_end():
                    self._winner = self._current_state._MIN_TOKEN
                self._turn *= -1
            
            self._current_state.update_stage()
        
        print(f"Pobedio je igrač sa {self._winner} tokenom!")

    def get_player_move(self):
        if self._current_state._stage == 1:
            start_point = None
            while True:
                try:
                    end_point = int(
                        input("Unesite polje na koje želite da postavite figuru: "))
                except ValueError:
                    print("Unos mora biti broj.")
                    continue
                move = (start_point, end_point)
                if not self._current_state.is_valid_move(move, self._current_state._MAX_TOKEN):
                    print("Neispravan potez.")
                    continue
                break
        else:
            while True:
                self._current_state.get_all_moves(
                    self._current_state._MAX_TOKEN)
                try:
                    start_point = int(input("Izaberite figuru: "))
                    end_point = int(
                        input("Unesite polje gde želite da pomerite figuru: "))
                except ValueError:
                    print("Unos mora biti broj.")
                    continue
                move = (start_point, end_point)
                if not self._current_state.is_valid_move(move, self._current_state._MAX_TOKEN):
                    print("Neispravan potez.")
                    continue
                break
        return move

    def handle_mill(self):
        enemy_points = self._current_state.get_all_tokens(
            self._current_state._MIN_TOKEN)
        while True:
            try:
                point = int(
                    input("Unesite broj polja sa kog želite da uklonite protivničku figuru: "))
            except ValueError:
                print("Unos mora biti broj.")
                continue
            if point not in enemy_points:
                print("Morate izabrati polje sa protivničkom figurom.")
                continue
            break
        self._current_state.set_position(point, 'x')
        self._current_state._min_pieces -= 1

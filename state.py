from hashmap import ChainedHashMap
from copy import deepcopy

class State(object):
    def __init__(self):
        self._board = ChainedHashMap(50)
        for i in range(24):
            self._board[i] = 'x'
        
        # Susedne tačke nam posle služe da vidimo da li je odigrani potez validan
        self._adjacent_points = ChainedHashMap(50)
        self._set_adjacent_points()

        # Sve moguce mice
        self._mills = [
            (0, 1, 2),
            (0, 9, 21),
            (21, 22, 23),
            (2, 14, 23),
            (3, 4, 5),
            (3, 10, 18),
            (18, 19, 20),
            (5, 13, 20),
            (6, 7, 8),
            (6, 11, 15),
            (15, 16, 17),
            (8, 12, 17),
            (1, 4, 7),
            (9, 10, 11),
            (16, 19, 22),
            (12, 13, 14)
        ]

        self._stage = 1 # Faza igre
        self._stage_counter = 0 # brojac faze, na 9 igra prelazi u drugu fazu
        self._max_pieces = 9 # Broj tokena maks igraca
        self._min_pieces = 9 # Broj tokena min igraca
        self._MAX_TOKEN = '@' # Token maks igraca
        self._MIN_TOKEN = '#' # Token min igraca

    # Podesava susedne tacke
    def _set_adjacent_points(self):
        self._adjacent_points[0] = (1, 9)
        self._adjacent_points[1] = (0, 4, 2)
        self._adjacent_points[2] = (1, 14)
        self._adjacent_points[3] = (4, 10)
        self._adjacent_points[4] = (1, 3, 5, 7)
        self._adjacent_points[5] = (4, 13)
        self._adjacent_points[6] = (7, 11)
        self._adjacent_points[7] = (4, 6, 8)
        self._adjacent_points[8] = (7, 12)
        self._adjacent_points[9] = (0, 10, 21)
        self._adjacent_points[10] = (3, 9, 11, 18)
        self._adjacent_points[11] = (6, 10, 15)
        self._adjacent_points[12] = (8, 13, 17)
        self._adjacent_points[13] = (5, 12, 14, 20)
        self._adjacent_points[14] = (2, 13, 23)
        self._adjacent_points[15] = (11, 16)
        self._adjacent_points[16] = (15, 17, 19)
        self._adjacent_points[17] = (12, 16)
        self._adjacent_points[18] = (10, 19)
        self._adjacent_points[19] = (16, 18, 20, 22)
        self._adjacent_points[20] = (13, 19)
        self._adjacent_points[21] = (9, 22)
        self._adjacent_points[22] = (19, 21, 23)
        self._adjacent_points[23] = (14, 22)
    
    # Vraca susedne tacke
    def get_adjacent_points(self):
        return self._adjacent_points
    
    # Proverava da li je neka tacka susedna
    # pov - point of view
    # point - tacka koju ispitujemo
    def is_adjacent_point(self, pov, point):
        if point in self._adjacent_points[pov]:
            return True
        return False
    
    # Menja poziciju na tabli
    # point - tacka koja se menja
    # token - token koji se postavlja na izabranu poziciju
    def set_position(self, point, token):
        self._board[point] = token
    
    # Vraca sve moguce mice
    def get_mills(self):
        return self._mills
    
    # Proverava da li postoji mica u trenutnoj poziciji
    # last_move - poslednje polje koje se promenilo
    def is_mill(self, last_move):
        mills = self.get_mills()
        for mill in mills:
            temp = [self._board[mill[0]], self._board[mill[1]], self._board[mill[2]]]
            result = temp.count(temp[0]) == len(temp)
            if result and (last_move in mill):
                return True
        return False
    
    # Proverava da li je u trenutnoj poziciji kraj
    def is_end(self):
        if self._max_pieces == 2 or self._min_pieces == 2:
            return True
        return False

    # HEURISTIKA
    # Procenjuje trenutnu poziciju
    def evaluate(self):
        return self._max_pieces - self._min_pieces
    
    # Vraca sva moguca grananja trenutnog stanja
    # turn - igrac na potezu
    def get_states(self, turn):
        pass

    # Proverava da li je potez validan
    # move - potez koji se proverava
    # token - igracev token
    def is_valid_move(self, move, token):
        if self._stage == 1:
            point = move[1] # (start_point, end_point)
            if self._board[point] != 'x':
                return False
        else:
            (start_point, end_point) = move
            if self._board[start_point] != token and self._board[end_point] != 'x':
                return False
        return True
    
    # Simulacija poteza
    # move - potez
    # token - igracev token
    def simulate_move(self, move, token):
        if self.is_valid_move(move, token):
            (start_point, end_point) = move
            self.set_position(end_point, token)
            if self._stage != 1:
                self.set_position(start_point, 'x')

    # Ispisivanje table
    def __str__(self):
        return f"""
        {self._board[0]}-----{self._board[1]}-----{self._board[2]}\t0, 1, 2
        |     |     |
        | {self._board[3]}---{self._board[4]}---{self._board[5]} |\t3, 4, 5
        | |   |   | |
        | | {self._board[6]}-{self._board[7]}-{self._board[8]} | |\t6, 7, 8
        | | |   | | |
        {self._board[9]}-{self._board[10]}-{self._board[11]}   {self._board[12]}-{self._board[13]}-{self._board[14]}\t9, 10, 11, 12, 13, 14
        | | |   | | |
        | | {self._board[15]}-{self._board[16]}-{self._board[17]} | |\t15, 16, 17
        | |   |   | |
        | {self._board[18]}---{self._board[19]}---{self._board[20]} |\t18, 19, 20
        |     |     |
        {self._board[21]}-----{self._board[22]}-----{self._board[23]}\t21, 22, 23
        """

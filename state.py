from hashmap import ChainedHashMap


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
    
    def get_mills(self):
        return self._mills

    # Ispisivanje table
    def __str__(self):
        return f"""
        {self.board_map[0]}-----{self.board_map[1]}-----{self.board_map[2]}\t0, 1, 2
        |     |     |
        | {self.board_map[3]}---{self.board_map[4]}---{self.board_map[5]} |\t3, 4, 5
        | |   |   | |
        | | {self.board_map[6]}-{self.board_map[7]}-{self.board_map[8]} | |\t6, 7, 8
        | | |   | | |
        {self.board_map[9]}-{self.board_map[10]}-{self.board_map[11]}   {self.board_map[12]}-{self.board_map[13]}-{self.board_map[14]}\t9, 10, 11, 12, 13, 14
        | | |   | | |
        | | {self.board_map[15]}-{self.board_map[16]}-{self.board_map[17]} | |\t15, 16, 17
        | |   |   | |
        | {self.board_map[18]}---{self.board_map[19]}---{self.board_map[20]} |\t18, 19, 20
        |     |     |
        {self.board_map[21]}-----{self.board_map[22]}-----{self.board_map[23]}\t21, 22, 23
        """

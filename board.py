from hashmap import ChainedHashMap


class Board(object):
    def __init__(self):
        self._board = ChainedHashMap(30)
        for i in range(24):
            self._board[i] = 'x'
        
        # Susedne tačke nam posle služe da vidimo da li je odigrani potez validan
        self._adjacent_points = ChainedHashMap()
        for i in range(24):
            self._adjacent_points[i] = None
        self.set_adjacent_points(self._adjacent_points)

    def set_adjacent_points(self, points):
        points[0] = (1, 9)
        points[1] = (0, 4, 2)
        points[2] = (1, 14)
        points[3] = (4, 10)
        points[4] = (1, 3, 5, 7)
        points[5] = (4, 13)
        points[6] = (7, 11)
        points[7] = (4, 6, 8)
        points[8] = (7, 12)
        points[9] = (0, 10, 21)
        points[10] = (3, 9, 11, 18)
        points[11] = (6, 10, 15)
        points[12] = (8, 13, 17)
        points[13] = (5, 12, 14, 20)
        points[14] = (2, 13, 23)
        points[15] = (11, 16)
        points[16] = (15, 17, 19)
        points[17] = (12, 16)
        points[18] = (10, 19)
        points[19] = (16, 18, 20, 22)
        points[20] = (13, 19)
        points[21] = (9, 22)
        points[22] = (19, 21, 23)
        points[23] = (14, 22)

    def get_pos(self, coordinates):
        return self._board[coordinates]

    def set_pos(self, coordinates, piece):
        self._board[coordinates] = piece

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
        {self._board[0]}-----{self._board[1]}-----{self._board[2]}\t21, 22, 23
        """

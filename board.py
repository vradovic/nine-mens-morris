from hashmap import ChainedHashMap


class Board(object):
    def __init__(self):
        self.board_map = ChainedHashMap(50)
        for i in range(24):
            self.board_map[i] = 'x'
        
        # Susedne tačke nam posle služe da vidimo da li je odigrani potez validan
        self._adjacent_points = ChainedHashMap(50)
        self._set_adjacent_points(self._adjacent_points)

    def _set_adjacent_points(self, points):
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
    
    def is_adjacent_point(self, start, end):
        if end in self._adjacent_points[start]:
            return True
        return False

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

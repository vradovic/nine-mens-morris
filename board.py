from hashmap import ChainedHashMap


class Board(object):
    def __init__(self):
        self._board = ChainedHashMap(30)
        for i in range(24):
            self._board[i] = 'x'

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

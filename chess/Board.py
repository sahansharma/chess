class Board:
    def __init__(self):
        self._pawn_position = 'a1'
        self._queen_position = 'a1'

    def add_pawn(self, pos):
        self._pawn_position = pos

    def piece_type(self, pos):
        if self._pawn_position == pos:
            return 'pawn'
        if self._queen_position == pos:
            return 'queen'
        return 'empty'

    def add_queen(self, pos):
        self._queen_position = pos

    def add(self, pos, piece_name):
        if piece_name == 'pawn':
            self._pawn_position = pos
        elif piece_name == 'queen':
            self._queen_position = pos

    def move(self, from_pos, to_pos):
        if self._pawn_position == from_pos:
            self._pawn_position = to_pos
        elif self._queen_position == from_pos:
            self._queen_position = to_pos

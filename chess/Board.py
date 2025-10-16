class Board:
    def __init__(self):
        self._pawn_position = 'a1'
        self._queen_position = 'a1'

    def add_pawn(self, pos: str):
        self._pawn_position = pos

    def piece_type(self, pos: str):
        if self._pawn_position == pos:
            return 'pawn'
        if self._queen_position == pos:
            return 'queen'
        return 'empty'

    def add_queen(self, pos: str):
        self._queen_position = pos

    def add(self, pos: str, piece_name: str):
        if piece_name == 'pawn':
            self._pawn_position = pos
        elif piece_name == 'queen':
            self._queen_position = pos

    def move(self, from_pos: str, to_pos: str):
        if self._pawn_position == from_pos:
            self._pawn_position = to_pos
        elif self._queen_position == from_pos:
            self._queen_position = to_pos

    def iterate_pieces(self):
        return []

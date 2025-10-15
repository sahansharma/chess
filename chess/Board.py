class Board:
    def __init__(self):
        self._pawn_position = 'a1'

    def move_pawn(self, from_pos, pos):
        self._pawn_position = pos

    def add_pawn(self, pos):
        self._pawn_position = pos

    def piece_type(self, pos):
        if self._pawn_position == pos:
            return 'pawn'
        return 'empty'


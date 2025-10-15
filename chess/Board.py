class Board:
    def __init__(self):
        self._pawn_position = 'a1'
        self._queen_position = 'a1'

    def move_pawn(self, from_pos, pos):
        self._pawn_position = pos

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

    def move_queen(self, from_pos, to_pos):
            self._queen_position = to_pos
    

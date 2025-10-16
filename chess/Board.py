class Board:
    def __init__(self):
        self._pieces = {}

    def add_pawn(self, pos: str):
        self._pieces[pos] = 'pawn'

    def piece_type(self, pos: str):
        return self._pieces.get(pos, 'empty')

    def add_queen(self, pos: str):
        self._pieces[pos] = 'queen'

    def add(self, pos: str, piece_name: str):
        self._pieces[pos] = piece_name

    def move(self, from_pos: str, to_pos: str):
        piece = self._pieces.pop(from_pos)
        self._pieces[to_pos] = piece

    def iterate_pieces(self) -> list[str]:
        return [*self._pieces.keys()]

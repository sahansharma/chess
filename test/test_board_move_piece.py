from chess.Board import Board


def test_player_moves_pawn():
  board = Board()
  board.add_pawn('e3')
  board.move_pawn('e3', 'e4')
  # then the pawn is at e4
  assert board.piece_type('e4') == 'pawn'

def test_player_moves_pawn_away_from_field():
  # given pawn is initially at e3
  board = Board()
  board.add_pawn('e3')
  # when the player moves pawn away from e3
  board.move_pawn('e3', 'e4')
  # then the pawn is not at e3
  assert board.piece_type('e3') == 'empty'

def test_user_moves_queen_diagonally():
    board = Board()
    board.add_queen('e3')
    board.move_queen('e3', 'g5')
    assert board.piece_type('g5') =='queen'
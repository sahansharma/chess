from chess.Board import Board


def test_player_moves_pawn():
  # given pawn is initially at e3
  board = Board()
  board.add_pawn('e3')
  # when the player moves pawn from e3 to e4
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

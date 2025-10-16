import pytest
from chess.Board import Board


@pytest.fixture
def board():
  """Creates a fresh instance of board before each test."""
  return Board()

def test_player_moves_pawn(board):
  board.add('e3','pawn')
  board.move('e3', 'e4')
  # then the pawn is at e4
  assert board.piece_type('e4') == 'pawn'

def test_player_moves_pawn_away_from_field(board):
  board.add('e3', 'pawn')
  # when the player moves pawn away from e3
  board.move('e3', 'e4')
  # then the pawn is not at e3
  assert board.piece_type('e3') == 'empty'

def test_user_moves_queen_diagonally(board):
    board.add('e3', 'queen')
    board.move('e3', 'g5')
    assert board.piece_type('g5') =='queen'

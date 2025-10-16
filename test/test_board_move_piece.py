from pytest import fixture

from chess.Board import Board

@fixture
def board():
    return Board()

def test_player_moves_pawn(board: Board):
    board.add('e3', 'pawn')
    board.move('e3', 'e4')
    # then the pawn is at e4
    assert board.piece_type('e4') == 'pawn'

def test_player_moves_pawn_away_from_field(board: Board):
    board.add('e3', 'pawn')
    # when the player moves pawn away from e3
    board.move('e3', 'e4')
    # then the pawn is not at e3
    assert board.piece_type('e3') == 'empty'

def test_user_moves_queen_diagonally(board: Board):
    board.add('e3', 'queen')
    board.move('e3', 'g5')
    assert board.piece_type('g5') == 'queen'

def test_empty_board_has_no_pieces(board: Board):
    assert board.iterate_pieces() == []

def test_board_outputs_all_pieces(board: Board):
    board.add('b7', 'pawn')
    assert board.iterate_pieces() == ['b7']

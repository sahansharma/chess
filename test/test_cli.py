from chess.ChessCli import ChessCli
from chess.Board import Board

def test_empty_board():
    cli = ChessCli(Board())
    assert cli.board() == """
----------
|        |
|        |
|        |
|        |
|        |
|        |
|        |
|        |
----------
"""

def test_board_one_pawn():
    # given a pawn is at e3
    board = Board()
    board.add('pawn', 'b7')
    # when the cli is rendered
    cli = ChessCli(board)
    view = cli.board()
    # then the view contains a pawn at e3
    assert view == """
----------
|        |
| p      |
|        |
|        |
|        |
|        |
|        |
|        |
----------
"""

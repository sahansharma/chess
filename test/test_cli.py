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
    # given a pawn is at b7
    board = Board()
    board.add('b7', 'pawn')
    # when the cli is rendered
    cli = ChessCli(board)
    view = cli.board()
    # then the view contains a pawn at b7
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

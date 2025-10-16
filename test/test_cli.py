from chess.ChessCli import ChessCli

def test_board():
    cli = ChessCli()
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

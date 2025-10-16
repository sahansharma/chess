from chess.Board import Board

class ChessCli:
    def __init__(self, board: Board):
        self._board = board

    def board(self) -> str:
        board_lines = [
            "|        |",
            "|        |",
            "|        |",
            "|        |",
            "|        |",
            "|        |",
            "|        |",
            "|        |",
        ]
        if self._board._pawn_position == "b7":
            board_lines[1] = "| p      |"
        return "\n" + "\n".join(["----------"] + board_lines + ["----------"]) + "\n"

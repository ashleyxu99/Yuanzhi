class Player1:
    """Player1"""
    def __init__(self, board, game_controller):
        self.board = board
        self.gc = game_controller

    def move(self, x, y):
        """Handle keyboard input for Player1"""
        # Try to put a black tile at the mouse-specifid position
        self.board.put_tile(x, y, 0)

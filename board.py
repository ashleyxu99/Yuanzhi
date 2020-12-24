from tiles import Tiles


class Board:
    """A tile board"""
    def __init__(self, WIDTH, HEIGHT, game_controller):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = 100
        self.COLS = self.WIDTH // self.SPACING
        self.ROWS = self.HEIGHT // self.SPACING
        self.squares = Tiles(self.COLS, self.ROWS)
        # Control the interation between players and tiles
        self.gc = game_controller

    def display(self):
        """Display the board and make necessary per-frame updates"""
        # Draw the board lines
        stroke(0)
        strokeWeight(3)
        for i in range(self.ROWS-1):
            line(0, (i + 1) * 100, self.WIDTH, (i + 1) * 100)
        for j in range(self.COLS-1):
            line((j + 1) * 100, 0, (j + 1) * 100, self.HEIGHT)

        # Draw the tiles
        self.squares.display()

        # Make necessary per-frame updates
        self.update()

    def update(self):
        """Make necessary per-frame updates"""
        # If the game is not over
        if not self.gc.game_over:
            # Check whether the board has legal moves left
            black_flips_left = False
            white_flips_left = False
            for i in range(len(self.squares.tiles)):
                for j in range(len(self.squares.tiles[i])):
                    if ((not black_flips_left) and
                       (self.search_flips(j, i, 0))):
                        black_flips_left = True
                    if ((not white_flips_left) and
                       (self.search_flips(j, i, 1))):
                        white_flips_left = True

            # If the human's (player1's) turn
            if self.gc.player1_turn:
                # And if there are no more legal moves
                if not black_flips_left:
                    # Switch back to the computer (player2)
                    self.gc.player1_turn = False

            # If the computer's (player2's) turn
            if not self.gc.player1_turn:
                # And if there are no legal moves
                if not white_flips_left:
                    # Switch back to the human (player1)
                    self.gc.player1_turn = True

            # If there are no more legal moves at all
            if (not black_flips_left) and (not white_flips_left):
                # End the game
                self.gc.game_over = True

        # Collect the players scores
        self.gc.player1_score = self.squares.tile_counts["black"]
        self.gc.player2_score = self.squares.tile_counts["white"]

    def put_tile(self, x, y, color):
        """Put a new tile on the board if the move is legal"""
        col = x // self.SPACING
        row = y // self.SPACING
        # Search for flips of the current move
        flips = self.search_flips(col, row, color)

        # Check if there are legal flips for the current move
        if flips:
            # Put a tile
            self.squares.put_tile(col, row, color)
            # Flip the corresponding opposing tiles
            self.squares.flip_tiles(color, flips)
            # It's another player's turn
            self.gc.player1_turn = not self.gc.player1_turn
            # Reset the delay_counter
            self.gc.delay_counter = 90

    def search_flips(self, col, row, color):
        """Search for flips for the current move"""
        # Keep track of the flips in all the 8 directions for the current move
        flips = {}

        # First, check if the square is empty
        if not self.squares.tiles[row][col]:
            # Next, check if it would end up flipping any opposing tiles
            # Check top
            potential_flips = []
            row_i = row
            while ((row_i - 1 != -1) and
                   (self.squares.tiles[row_i-1][col]) and
                   (self.squares.tiles[row_i-1][col].color != color)):
                potential_flips.append((row_i-1, col))
                row_i -= 1

            if ((potential_flips) and
               (row_i - 1 != -1) and
               (self.squares.tiles[row_i-1][col]) and
               (self.squares.tiles[row_i-1][col].color == color)):
                flips["top"] = potential_flips
                row_i -= 1

            # Check left
            potential_flips = []
            col_i = col
            while ((col_i - 1 != -1) and
                   (self.squares.tiles[row][col_i-1]) and
                   (self.squares.tiles[row][col_i-1].color != color)):
                potential_flips.append((row, col_i-1))
                col_i -= 1

            if ((potential_flips) and
               (col_i - 1 != -1) and
               (self.squares.tiles[row][col_i-1]) and
               (self.squares.tiles[row][col_i-1].color == color)):
                flips["left"] = potential_flips
                col_i -= 1

            # Check bottom
            potential_flips = []
            row_i = row
            while ((row_i + 1 < self.ROWS) and
                   (self.squares.tiles[row_i+1][col]) and
                   (self.squares.tiles[row_i+1][col].color != color)):
                potential_flips.append((row_i+1, col))
                row_i += 1

            if ((potential_flips) and
               (row_i + 1 < self.ROWS) and
               (self.squares.tiles[row_i+1][col]) and
               (self.squares.tiles[row_i+1][col].color == color)):
                flips["bottom"] = potential_flips
                row_i += 1

            # Check right
            potential_flips = []
            col_i = col
            while ((col_i + 1 < self.COLS) and
                   (self.squares.tiles[row][col_i+1]) and
                   (self.squares.tiles[row][col_i+1].color != color)):
                potential_flips.append((row, col_i+1))
                col_i += 1

            if ((potential_flips) and
               (col_i + 1 < self.COLS) and
               (self.squares.tiles[row][col_i+1]) and
               (self.squares.tiles[row][col_i+1].color == color)):
                flips["right"] = potential_flips
                col_i += 1

            # Check topleft
            potential_flips = []
            row_i = row
            col_i = col
            while ((row_i - 1 != -1) and (col_i - 1 != -1) and
                   (self.squares.tiles[row_i-1][col_i-1]) and
                   (self.squares.tiles[row_i-1][col_i-1].color != color)):
                potential_flips.append((row_i-1, col_i-1))
                row_i -= 1
                col_i -= 1

            if ((potential_flips) and
               (row_i - 1 != -1) and (col_i - 1 != -1) and
               (self.squares.tiles[row_i-1][col_i-1]) and
               (self.squares.tiles[row_i-1][col_i-1].color == color)):
                flips["topleft"] = potential_flips
                row_i -= 1
                col_i -= 1

            # Check bottomleft
            potential_flips = []
            row_i = row
            col_i = col
            while ((row_i + 1 < self.ROWS) and (col_i - 1 != -1) and
                   (self.squares.tiles[row_i+1][col_i-1]) and
                   (self.squares.tiles[row_i+1][col_i-1].color != color)):
                potential_flips.append((row_i+1, col_i-1))
                row_i += 1
                col_i -= 1

            if ((potential_flips) and
               (row_i + 1 < self.ROWS) and (col_i - 1 != -1) and
               (self.squares.tiles[row_i+1][col_i-1]) and
               (self.squares.tiles[row_i+1][col_i-1].color == color)):
                flips["bottomleft"] = potential_flips
                row_i += 1
                col_i -= 1

            # Check bottomright
            potential_flips = []
            row_i = row
            col_i = col
            while ((row_i + 1 < self.ROWS) and (col_i + 1 < self.COLS) and
                   (self.squares.tiles[row_i+1][col_i+1]) and
                   (self.squares.tiles[row_i+1][col_i+1].color != color)):
                potential_flips.append((row_i+1, col_i+1))
                row_i += 1
                col_i += 1

            if ((potential_flips) and
               (row_i + 1 < self.ROWS) and (col_i + 1 < self.COLS) and
               (self.squares.tiles[row_i+1][col_i+1]) and
               (self.squares.tiles[row_i+1][col_i+1].color == color)):
                flips["bottomright"] = potential_flips
                row_i += 1
                col_i += 1

            # Check topright
            potential_flips = []
            row_i = row
            col_i = col
            while ((row_i - 1 != -1) and (col_i + 1 < self.COLS) and
                   (self.squares.tiles[row_i-1][col_i+1]) and
                   (self.squares.tiles[row_i-1][col_i+1].color != color)):
                potential_flips.append((row_i-1, col_i+1))
                row_i -= 1
                col_i += 1

            if ((potential_flips) and
               (row_i - 1 != -1) and (col_i + 1 < self.COLS) and
               (self.squares.tiles[row_i-1][col_i+1]) and
               (self.squares.tiles[row_i-1][col_i+1].color == color)):
                row_i -= 1
                col_i += 1
                flips["topright"] = potential_flips

        return flips

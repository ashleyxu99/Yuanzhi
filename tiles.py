from tile import Tile


class Tiles:
    """A collection of tiles"""
    def __init__(self, COLS, ROWS):
        self.COLS = COLS
        self.ROWS = ROWS

        # Create an empty collection of tiles
        self.tiles = [
            [None for _ in range(self.COLS)] for _ in range(self.ROWS)
        ]

        # Put 4 tiles at the beginning of the game
        self.tiles[self.ROWS//2-1][self.COLS//2-1] = Tile(
            self.COLS//2-1, self.ROWS//2-1, 1
        )
        self.tiles[self.ROWS//2][self.COLS//2] = Tile(
            self.COLS//2, self.ROWS//2, 1
        )
        self.tiles[self.ROWS//2-1][self.COLS//2] = Tile(
            self.COLS//2, self.ROWS//2-1, 0
        )
        self.tiles[self.ROWS//2][self.COLS//2-1] = Tile(
            self.COLS//2-1, self.ROWS//2, 0
        )

        # Keep track of the number of black tiles and white tiles
        self.tile_counts = {"black": 2, "white": 2}

    def display(self):
        """Draw a collection of tiles"""
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j]:
                    self.tiles[i][j].display()

    def put_tile(self, col, row, color):
        """Put a new tile in the collection"""
        # Initiate a new tile in the tiles collection
        self.tiles[row][col] = Tile(
            col, row, color
        )
        # Updates the corresponding tile count
        if color == 0:
            self.tile_counts["black"] += 1
        else:
            self.tile_counts["white"] += 1

    def flip_tiles(self, color, flips):
        """Flip all the opposing tiles in the flips dictionary"""
        # Loop through every the possible direction
        for direction in flips.keys():
            # Loop through every possible to-be-flipped tile in this direction
            for row_col in flips[direction]:
                # Update the corresponding tile count
                if self.tiles[row_col[0]][row_col[1]].color == 0:
                    self.tile_counts["black"] -= 1
                else:
                    self.tile_counts["white"] -= 1
                # Remove the opposing tile
                self.tiles[row_col[0]][row_col[1]] = None
                # Put a new tile
                self.put_tile(row_col[1], row_col[0], color)

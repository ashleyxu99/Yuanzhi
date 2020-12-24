class Tile:
    """A tile"""
    def __init__(self, column, row, color):
        self.column = column
        self.row = row
        self.color = color

    def display(self):
        """Draw the tile"""
        stroke(0)
        strokeWeight(3)
        fill(self.color)
        ellipse(self.column * 100 + 50, self.row * 100 + 50, 90, 90)

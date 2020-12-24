from board import Board
from game_controller import GameController


def test_constructor():
    """ test the constructor of Board"""
    gc = GameController(800, 800)
    b = Board(800, 800, gc)
    assert b.WIDTH == 800
    assert b.HEIGHT == 800
    assert b.SPACING == 100
    assert b.COLS == 8
    assert b.ROWS == 8
    assert b.squares.tile_counts["white"] == 2
    assert b.squares.tile_counts["black"] == 2
    assert b.gc is gc


def test_put_tiles():
    """ test the put titles method"""
    gc1 = GameController(800, 800)
    b1 = Board(800, 800, gc1)
    gc2 = GameController(800, 800)
    b2 = Board(800, 800, gc2)
    # Illegal move.
    b1.put_tile(0, 0, 0)
    # Legal move.
    b2.put_tile(200, 300, 0)
    assert b1.squares.tiles[0][0] is None
    assert b1.squares.tiles[3][3].color == 1
    assert b1.squares.tile_counts["black"] == 2
    assert b1.squares.tile_counts["white"] == 2
    assert b2.squares.tiles[3][2].color == 0
    assert b2.squares.tiles[3][3].color == 0
    assert b2.squares.tile_counts["black"] == 4
    assert b2.squares.tile_counts["white"] == 1


def test_search_flips():
    """ test the search flips method"""
    gc1 = GameController(800, 800)
    b1 = Board(800, 800, gc1)
    gc2 = GameController(800, 800)
    b2 = Board(800, 800, gc2)
    # Illegal move.
    flips1 = b1.search_flips(0, 0, 0)
    # Legal move.
    flips2 = b2.search_flips(2, 3, 0)
    assert flips1 == {}
    assert flips2["right"] == [(3, 3)]

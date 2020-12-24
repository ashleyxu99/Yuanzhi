from tiles import Tiles


def test_constructor():
    """ test the titles constructor"""
    ts = Tiles(8, 8)
    assert ts.COLS == 8
    assert ts.ROWS == 8
    for i in range(8):
        for j in range(8):
            if ((i == 3 and j == 3) or (i == 4 and j == 4)):
                assert ts.tiles[i][j].color == 1
            elif ((i == 3 and j == 4) or (i == 4 and j == 3)):
                assert ts.tiles[i][j].color == 0
            else:
                assert ts.tiles[i][j] is None
    assert ts.tile_counts["black"] == 2
    assert ts.tile_counts["white"] == 2


def test_put_tile():
    """ test the put titles method"""
    ts = Tiles(8, 8)
    ts.put_tile(0, 0, 0)
    assert ts.tiles[0][0].color == 0
    assert ts.tile_counts["black"] == 3


def test_flip_tiles():
    """ test the flip titles method"""
    ts = Tiles(8, 8)
    flips = {"right": [(3, 3)]}
    ts.flip_tiles(0, flips)
    assert ts.tiles[3][3].color == 0
    assert ts.tile_counts["white"] == 1
    assert ts.tile_counts["black"] == 3

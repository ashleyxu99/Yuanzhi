from tile import Tile


def test_constructor():
    """ test the tile constructor"""
    t = Tile(3, 4, 1)
    assert t.column == 3
    assert t.row == 4
    assert t.color == 1

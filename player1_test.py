from board import Board
from game_controller import GameController
from player1 import Player1


def test_constructor():
    """ test the player1 constructor"""
    gc = GameController(800, 800)
    b = Board(800, 800, gc)
    p1 = Player1(b, gc)
    assert p1.board is b
    assert p1.gc is gc


def test_move():
    """ test the move method"""
    gc = GameController(800, 800)
    b = Board(800, 800, gc)
    p1 = Player1(b, gc)
    # Illegal move.
    p1.move(0, 0)
    assert p1.board.squares.tiles[0][0] is None
    assert p1.board.squares.tiles[3][3].color == 1
    assert p1.board.squares.tile_counts["black"] == 2
    assert p1.board.squares.tile_counts["white"] == 2
    # Legal move.
    p1.move(200, 300)
    assert p1.board.squares.tiles[3][2].color == 0
    assert p1.board.squares.tiles[3][3].color == 0
    assert p1.board.squares.tile_counts["black"] == 4
    assert p1.board.squares.tile_counts["white"] == 1

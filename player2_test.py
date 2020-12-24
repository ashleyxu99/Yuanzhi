from board import Board
from game_controller import GameController
from player2 import Player2


def test_constructor():
    """ test the constructor of player2"""
    gc = GameController(800, 800)
    b = Board(800, 800, gc)
    p2 = Player2(b, gc)
    assert p2.board is b
    assert p2.gc is gc


def test_move():
    """ test the move method"""
    gc = GameController(800, 800)
    b = Board(800, 800, gc)
    p2 = Player2(b, gc)
    p2.move()
    assert p2.board.squares.tile_counts["black"] == 1
    assert p2.board.squares.tile_counts["white"] == 4

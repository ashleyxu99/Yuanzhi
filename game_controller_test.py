from game_controller import GameController


def test_constructor():
    """ test the constructor of game controller"""
    gc = GameController(800, 800)
    assert gc.WIDTH == 800
    assert gc.HEIGHT == 800
    assert gc.player1_turn
    assert not gc.game_over
    assert gc.player1_score == 2
    assert gc.player2_score == 2
    assert gc.delay_counter == 100
    assert not gc.is_saved
    assert gc.delay_counter2 == 120
